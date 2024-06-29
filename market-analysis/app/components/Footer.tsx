"use client";

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white py-8">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="text-center md:text-left mb-4 md:mb-0">
            <p className="text-lg font-bold">Market Analysis</p>
            <p>© 2024 Market Analysis. All rights reserved.</p>
            <p>
              <a href="mailto:support@marketanalysis.com" className="text-gray-400 hover:text-white">support@marketanalysis.com</a>
            </p>
          </div>
          <div className="flex space-x-4">
            <a href="/privacy-policy" className="text-gray-400 hover:text-white">Privacy Policy</a>
            <a href="/terms-of-service" className="text-gray-400 hover:text-white">Terms of Service</a>
            <a href="/contact-us" className="text-gray-400 hover:text-white">Contact Us</a>
          </div>
        </div>
        <div className="flex justify-center space-x-6 mt-4">
        <a href="https://github.com/yourprofile" className="text-gray-400 hover:text-white mx-2">
              <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.727-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.757-1.333-1.757-1.087-.743.083-.727.083-.727 1.205.085 1.84 1.238 1.84 1.238 1.07 1.835 2.81 1.305 3.495.998.107-.775.418-1.305.76-1.605-2.665-.305-5.467-1.332-5.467-5.93 0-1.31.467-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23a11.45 11.45 0 013.005-.404c1.02.005 2.045.137 3.005.404 2.28-1.552 3.285-1.23 3.285-1.23.65 1.653.25 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.62-5.475 5.92.435.375.81 1.108.81 2.23 0 1.61-.015 2.91-.015 3.31 0 .315.215.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12" />
              </svg>
            </a>
            <a href="https://www.linkedin.com/yourprofile" className="text-gray-400 hover:text-white mx-2">
              <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M22.23 0H1.77C.79 0 0 .774 0 1.725v20.549C0 23.226.79 24 1.77 24h20.459C23.21 24 24 23.226 24 22.274V1.725C24 .774 23.21 0 22.23 0zM7.122 20.452H3.656V9.098h3.466v11.354zm-1.733-12.85a2.003 2.003 0 110-4.006 2.003 2.003 0 010 4.006zM20.452 20.452h-3.466V14.75c0-1.365-.025-3.122-1.9-3.122-1.905 0-2.197 1.48-2.197 3.014v5.81h-3.466V9.098h3.329v1.547h.048c.464-.878 1.597-1.8 3.287-1.8 3.514 0 4.166 2.313 4.166 5.321v6.286z" />
              </svg>
            </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;


