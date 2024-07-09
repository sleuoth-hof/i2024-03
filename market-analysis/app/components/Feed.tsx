"use client";
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UpdateCard from './UpdateCard';
import InfiniteScroll from 'react-infinite-scroll-component'; // npm install --save react-infinite-scroll-component

const FeedSection: React.FC = () => {
  const [articles, setArticles] = useState<any[]>([]);
  const [selectedArticle, setSelectedArticle] = useState<any | null>(null);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [page, setPage] = useState<number>(1); 

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await axios.get<any[]>('http://127.0.0.1:8000/article/', {
          params: { page: page, limit: 5 } 
        });
        setArticles((prevArticles) => [...prevArticles, ...response.data]); 
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    };

    fetchArticles();
  }, [page]);

  const handleArticleClick = (article: any) => {
    setSelectedArticle(article);
  };

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  const filteredArticles = articles.filter((article) =>
    article.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const fetchMoreData = () => {
    setPage(page + 1); 
  };

  return (
    <section id="feed" className="min-h-screen flex flex-col items-start justify-start bg-gray-800 py-8 mt-0">
      <div className="container mx-auto px-4">
        <h2 className="text-2xl font-bold text-white mb-4">Feed</h2>
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
          <div className="col-span-1 lg:col-span-1 bg-gray-900 text-white p-6 rounded-lg shadow-lg overflow-y-auto">
            <div className="mb-4">
              <input
                type="text"
                placeholder="Search updates..."
                className="w-full p-2 rounded-lg border border-gray-400 text-gray-800"
                value={searchTerm}
                onChange={handleSearchChange}
              />
            </div>
            <InfiniteScroll
              dataLength={filteredArticles.length}
              next={fetchMoreData}
              hasMore={true} 
              loader={<h4>Loading...</h4>}
              height={400} 
              endMessage={<p>No more articles</p>}
            >
              {filteredArticles.map((article: any) => (
                <div key={article.id} onClick={() => handleArticleClick(article)}>
                  <UpdateCard
                    title={article.title}
                    description={article.article_text}
                    date={article.formatted_date}
                    link={article.link}
                  />
                </div>
              ))}
            </InfiniteScroll>
          </div>
          <div className="col-span-2 lg:col-span-2 bg-gray-900 text-white p-6 rounded-lg shadow-lg">
            <div className="bg-gray-800 p-4 rounded-lg border border-gray-400 h-96 overflow-y-auto">
              {selectedArticle && (
                <>
                  <h3 className="text-xl font-bold mb-2">{selectedArticle.title}</h3>
                  <p className="">{selectedArticle.article_text}</p>
                  <p className="text-sm mt-2 text-blue-500">
                    <a
                      href={selectedArticle.link}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {selectedArticle.link}
                    </a>
                  </p>
                  <p className="text-xs mt-1 text-gray-500">
                    {selectedArticle.formatted_date}
                  </p>
                </>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FeedSection;