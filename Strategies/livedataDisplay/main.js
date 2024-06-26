google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);
//source: https://developers.google.com/chart/interactive/docs/basic_load_libs    google dokumentation for charts 
 //https://developers.google.com/chart/interactive/docs/gallery/candlestickchart  candelstick

    let data;
    let chart;
    let options;
 
    function drawChart() {
      data = new google.visualization.DataTable();
      data.addColumn('datetime', 'Zeit');
      data.addColumn('number', 'Low');
      data.addColumn('number', 'Open');
      data.addColumn('number', 'Close');
      data.addColumn('number', 'High');

      options = {
        title: 'trading bot',
        legend: 'none',
        hAxis: {
          format: 'HH:mm:ss',
          title: 'Time'
        },
        vAxis: {
          title: 'Price'
        },
        candlestick: {
          fallingColor: { strokeWidth: 0, fill: 'red' }, 
          risingColor: { strokeWidth: 0, fill: 'green' }  
        }
      };

      chart = new google.visualization.CandlestickChart(document.getElementById('chart_div'));
      chart.draw(data, options);

     
      startWebsocket();
    }

    function updateChart(timestamp, low, open, close, high) {
      data.addRow([new Date(timestamp),
         low, open, close, high]);
      chart.draw(data, options);
    }

    function startWebsocket() {
                //finnhub api
      const wsUrl = "wss://ws.finnhub.io?token=cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70";

      const ws = new WebSocket(wsUrl);

      ws.onopen = function() {

        ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}');
      };

      ws.onmessage = function(event) {
        const message = JSON.parse(event.data);
        if ('data' in message) {
          const trades = message.data;
          const low = Math.min(...trades.map(trade => trade.p));
          const high = Math.max(...trades.map(trade => trade.p));
          const open = trades[0].p;
          const close = trades[trades.length - 1].p;
          const timestamp = trades[0].t;

          updateChart(timestamp, low, open, close, high);
        }
      };

      ws.onerror = function(error) {
        console.log('WebSocket' + error);
      };

      ws.onclose = function() {
        console.log("Websocket closed ");
      };
    }