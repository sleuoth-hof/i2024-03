import React from 'react';

const StockSymbols: React.FC = () => {
  return (
    <section id="stocksymbols" className="min-h-screen flex flex-col items-start justify-start bg-gray-100 py-8 mt-16">
      <div className="container mx-auto px-4">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Stock Symbols</h2>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <div className="col-span-1 lg:col-span-1 bg-white p-6 rounded-lg shadow-lg">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Stocks List</h3>
            <div className="mb-4 flex">
              <input
                type="text"
                placeholder="Search Stocks..."
                className="w-full p-2 rounded-lg border border-gray-400"
              />
              <button className="ml-2 bg-gray-700 text-white px-4 py-2 rounded-lg hover:bg-gray-600">Search</button>
            </div>
          </div>
          <div className="col-span-1 lg:col-span-1 bg-white p-6 rounded-lg shadow-lg">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Graphical representation</h3>
            <div className="bg-white p-4 rounded-lg border border-gray-400 h-96 w-96 mx-auto">
              <p>Graph placeholder</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default StockSymbols;
