
"use client";
import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import Chart from 'chart.js/auto'; // Importiere Chart.js

const PredictionSection: React.FC = () => {
  const [chartData, setChartData] = useState<any[]>([]); 
  const [cashAmount, setCashAmount] = useState<number | null>(null); 
  const [positions, setPositions] = useState<any[]>([]);

  const chartRef = useRef<HTMLCanvasElement | null>(null); 
  const chartInstance = useRef<Chart | null>(null); 


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/tradeprice/');

        const data = response.data;
        setChartData(data); 
      } catch (error) {
        console.error('Error fetching trade price data:', error);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 20000); // 20 sec
    return () => clearInterval(interval); 
  }, []); 

  useEffect(() => {
    const fetchCashAmount = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/cash/2/');
        const data = response.data;

        setCashAmount(parseFloat(data.value)); 
      } catch (error) {
        console.error('Error fetching cash amount:', error);
      }
    };

    fetchCashAmount();
  }, []); 

  useEffect(() => {
    const fetchPositions = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/tradeprice/');
        const data = response.data;

        
        const boughtPositions = data.filter((entry: any) => entry.action === 'BUY');
        setPositions(boughtPositions); 

      } catch (error) {
        console.error('Error fetching bought positions:', error);
      }
    };

    fetchPositions();
  }, []); 

  useEffect(() => {
    if (!chartRef.current || chartData.length === 0) return;

    if (!chartInstance.current) {

      const ctx = chartRef.current.getContext('2d');

      if (ctx) {
        chartInstance.current = new Chart(ctx, {
          type: 'line',
          data: {
            labels: chartData.map((entry: any) => entry.timestamp),
            datasets: [
              {
                label: 'Current Price',
                data: chartData.map((entry: any) => parseFloat(entry.currentPrice)),
                borderColor: 'blue',
                backgroundColor: 'rgba(0, 0, 255, 0.1)',
                borderWidth: 2,
                pointRadius: 3,
                fill: false,
              },
              {
                label: 'Entry Price',
                data: chartData.map((entry: any) => parseFloat(entry.entryPrice)),
                borderColor: 'green',
                backgroundColor: 'rgba(0, 255, 0, 0.1)',
                borderWidth: 2,
                pointRadius: 3,
                fill: false,
              },
            ],
          },
          options: {
            responsive: true,
            plugins: {
              tooltip: {
                mode: 'index',
                intersect: false,
              },
            },
            scales: {
              x: {
                display: true,
                title: {
                  display: true,
                  text: 'Timestamp',
                },
              },
              y: {
                display: true,
                title: {
                  display: true,
                  text: 'Price',
                },
              },
            },
          },
        });
      }
    } else {
    
      chartInstance.current.data.labels = chartData.map((entry: any) => entry.timestamp);
      chartInstance.current.data.datasets[0].data = chartData.map((entry: any) => parseFloat(entry.currentPrice));
      
      chartInstance.current.data.datasets[1].data = chartData.map((entry: any) => parseFloat(entry.entryPrice));
      chartInstance.current.update(); 
    }
  }, [chartData]); 

  return (
    <section id="prediction" className="min-h-screen flex flex-col items-start justify-start bg-gray-100 py-8 mt-0">
      <div className="container mx-auto px-4">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Trading Bot</h2>
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
          <div className="col-span-2 lg:col-span-2 bg-white p-6 rounded-lg shadow-lg">
            <div className="p-4 rounded-lg">
              <canvas ref={chartRef} id="myChart"></canvas>
            </div>
          </div>
          <div className="col-span-1 lg:col-span-1 bg-white p-6 rounded-lg shadow-lg">
            <div className="p-4 rounded-lg">
              <h3 className="text-lg font-semibold text-gray-800 mb-2">Cash Amount:</h3>
              <p className="text-xl font-bold text-back-600">
                {cashAmount !== null ? `$${cashAmount.toFixed(2)}` : 'Loading...'}
              </p>
              <h3 className="text-lg font-semibold text-gray-800 mt-4">Bought Positions:</h3>
              <ul>
                {positions.map((position: any, index: number) => (
                  <li key={index}>
                    <strong>{position.symbol}</strong>: Bought at ${position.entryPrice}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default PredictionSection;