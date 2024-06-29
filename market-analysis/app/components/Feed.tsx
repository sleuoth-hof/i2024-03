import React from 'react';
import UpdateCard from './UpdateCard';

const FeedSection: React.FC = () => {
  return (
    <section id="feed" className="min-h-screen flex flex-col items-start justify-start bg-gray-800 py-8 mt-0">
      <div className="container mx-auto px-4">
        <h2 className="text-2xl font-bold text-white mb-4">Feed</h2>
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
          <div className="col-span-1 lg:col-span-1 bg-gray-900 text-white p-6 rounded-lg shadow-lg">
            <div className="mb-4">
              <input
                type="text"
                placeholder="Search updates..."
                className="w-full p-2 rounded-lg border border-gray-400 text-gray-800"
              />
            </div>
            <div className="space-y-4">
              <UpdateCard title="CNBC News" description="Stock futures flat as investors look ahead to Fed decision, earnings." />
              <UpdateCard title="CNN News" description="Hong Kong stocks are back from the dead. Here's why." />
              <UpdateCard title="BBC News" description="Stock futures flat as investors look ahead to Fed decision, earnings." />
              <UpdateCard title="The Wall Street Journal" description="Stock futures flat as investors look ahead to Fed decision, earnings." />
            </div>
          </div>
          <div className="col-span-2 lg:col-span-2 bg-gray-900 text-white p-6 rounded-lg shadow-lg">
            <div className="bg-white p-4 rounded-lg border border-gray-400 h-96">
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FeedSection;
