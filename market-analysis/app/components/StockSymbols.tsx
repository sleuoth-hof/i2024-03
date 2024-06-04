import React from 'react';

const StockSymbols: React.FC = () => {
  return (
    <section id="stocksymbols" className="min-h-screen flex flex-col items-center justify-start bg-gray-100 py-8">
      <div className="container mx-auto px-4">
        <h2 className="text-2xl font-bold text-gray-800 mb-8 ml-12">Stock Symbols</h2>
        <div className="flex flex-wrap justify-center gap-8">
          {}
          <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Stocks List</h3>
            <div className="p-4 rounded-lg">
              <input 
                type="text" 
                placeholder="Search Stocks..." 
                className="w-full p-2 rounded-lg border border-gray-300"
              />
            </div>
          </div>
          {}
          <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Graphical representation</h3>
            <div className="p-4 rounded-lg" style={{ height: '24rem' }}>
              <input 
                type="text" 
                placeholder="Search ..." 
                className="w-full p-2 rounded-lg border border-gray-300"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default StockSymbols;
