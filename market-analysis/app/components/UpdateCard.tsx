import React from 'react';

interface UpdateCardProps {
  title: string;
  description: string;
  date: string; 
  link: string; 
}

const UpdateCard: React.FC<UpdateCardProps> = ({ title, description, date, link }) => {
  const shortenText = (text: string, maxLength: number) => {
    if (text.length > maxLength) {
      return text.slice(0, maxLength) + '...';
    }
    return text;
  };

  return (
    <div className="bg-gray-800 p-4 rounded-lg shadow-md mb-10">
      <h3 className="text-lg font-bold text-white mb-2">{title}</h3>
      <p className="text-gray-400 mb-2">{shortenText(description, 100)}</p>
      <div className="flex items-center justify-between">
        <p className="text-xs text-gray-500">{date}</p>
        <a href={link} className="text-sm text-blue-500 hover:underline" target="_blank" rel="noopener noreferrer">
          Read more
        </a>
      </div>
    </div>
  );
};

export default UpdateCard;
