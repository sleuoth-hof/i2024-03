import React from 'react';

const PredictionSection: React.FC = () => {
  return (
    <section id="prediction" className="min-h-screen flex flex-col items-start justify-start bg-gray-100 py-8 mt-0">
      <div className="container mx-auto px-4">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Trading Bot</h2>
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
          <div className="col-span-2 lg:col-span-2 bg-white p-6 rounded-lg shadow-lg">
            <div className="bg-gray-700 p-4 rounded-lg h-96">
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default PredictionSection;
