"use client";
import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import { FINNHUB_API_URL, FINNHUB_API_KEY } from '../../config';
import { List, AutoSizer, ListRowProps } from 'react-virtualized';
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

interface Stock {
  symbol: string;
  description: string;
}

const StockSymbols: React.FC = () => {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [filteredStocks, setFilteredStocks] = useState<Stock[]>([]);
  const [selectedStock, setSelectedStock] = useState<string | null>(null);
  const [chartData, setChartData] = useState<any>({});
  const chartRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const fetchStocks = async () => {
      try {
        const response = await axios.get(`${FINNHUB_API_URL}/stock/symbol`, {
          params: {
            exchange: 'US',
            token: FINNHUB_API_KEY,
          },
        });
        setStocks(response.data);
        setFilteredStocks(response.data.slice(0, 10));
      } catch (error) {
        console.error('Error fetching stocks:', error);
      }
    };

    fetchStocks();
  }, []);

  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    const searchTerm = e.target.value.toLowerCase();
    const filtered = stocks.filter((stock) =>
      stock.description.toLowerCase().includes(searchTerm)
    );
    setFilteredStocks(filtered.slice(0, 10));
  };

  const handleSelect = (stock: Stock) => {
    setSelectedStock(stock.symbol);
    console.log(`Selected stock: ${stock.symbol}`);
  };

  const handleShowChart = () => {
    if (selectedStock) {
      console.log(`Showing chart for: ${selectedStock}`);
      startWebSocket(selectedStock);
    }
  };

  const startWebSocket = (symbol: string) => {
    const wsUrl = `wss://ws.finnhub.io?token=${FINNHUB_API_KEY}`;
    const ws = new WebSocket(wsUrl);

    ws.onopen = () => {
      console.log(`WebSocket opened for ${symbol}`);
      ws.send(JSON.stringify({ type: 'subscribe', symbol }));
    };

    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if ('data' in message) {
        const trades = message.data;
        const low = Math.min(...trades.map((trade: any) => trade.p));
        const high = Math.max(...trades.map((trade: any) => trade.p));
        const open = trades[0].p;
        const close = trades[trades.length - 1].p;
        const timestamp = trades[0].t;

        console.log(`Received data for ${symbol}: ${low}, ${open}, ${close}, ${high}`);
        updateChart(timestamp, low, open, close, high);
      }
    };

    ws.onerror = (error) => {
      console.error(`WebSocket error for ${symbol}: ${error}`);
    };

    ws.onclose = () => {
      console.log(`WebSocket closed for ${symbol}`);
    };
  };

  const updateChart = (timestamp: number, low: number, open: number, close: number, high: number) => {
    setChartData((prevData: any) => {
      const newLabels = prevData.labels ? [...prevData.labels, new Date(timestamp * 1000).toLocaleDateString()] : [new Date(timestamp * 1000).toLocaleDateString()];
      const newDataset = prevData.datasets ? [...prevData.datasets[0].data, close] : [close];
      return {
        labels: newLabels,
        datasets: [
          {
            label: 'Stock Price',
            data: newDataset,
            borderColor: 'rgba(75,192,192,1)',
            fill: false,
          },
        ],
      };
    });
  };

  const rowRenderer = ({ key, index, style }: ListRowProps) => {
    const stock = filteredStocks[index];
    return (
      <div
        key={key}
        style={style}
        className={`cursor-pointer p-2 hover:bg-gray-200 ${selectedStock === stock.symbol ? 'bg-gray-300' : ''}`}
        onClick={() => handleSelect(stock)}
      >
        {stock.symbol}: {stock.description}
      </div>
    );
  };

  return (
    <section id="stocksymbols" className="min-h-screen flex flex-col items-start justify-start bg-gray-100 py-8 mt-16">
      <div className="container mx-auto px-4">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Stock Symbols</h2>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <div className="col-span-1 lg:col-span-1 bg-white p-6 rounded-lg shadow-lg">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Stocks List</h3>
            <div className="flex mb-4">
              <input
                type="text"
                placeholder="Search Stocks..."
                className="w-full p-2 rounded-lg border border-gray-400"
                onChange={handleSearch}
              />
              <button
                className="ml-2 bg-gray-700 text-gray-300 px-3 py-2 rounded-md text-base font-medium hover:bg-gray-600 hover:text-white" 
                onClick={handleShowChart}
              >
                Represent
              </button>
            </div>
            <div style={{ height: '400px' }}>
              <AutoSizer>
                {({ height, width }: { height: number, width: number }) => (
                  <List
                    width={width}
                    height={height}
                    rowCount={filteredStocks.length}
                    rowHeight={40}
                    rowRenderer={rowRenderer}
                  />
                )}
              </AutoSizer>
            </div>
          </div>
          <div className="col-span-1 lg:col-span-1 bg-white p-6 rounded-lg shadow-lg">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Graphical representation</h3>
            <div ref={chartRef} className="bg-white p-4 rounded-lg border border-gray-400 h-96 w-full">
              {chartData.labels ? (
                <Line data={chartData} />
              ) : (
                <p className="text-center">Select a stock to see the chart</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default StockSymbols;

