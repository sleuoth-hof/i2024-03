import React from 'react';

interface UpdateCardProps {
  title: string;
  description: string;
}

const UpdateCard: React.FC<UpdateCardProps> = ({ title, description }) => {
  return (
    <div className="bg-gray-800 p-4 rounded-lg shadow-md">
      <h3 className="text-lg font-bold text-white mb-2">{title}</h3>
      <p className="text-gray-400">{description}</p>
    </div>
  );
};

export default UpdateCard;
