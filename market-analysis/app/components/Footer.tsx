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
          </div>
        </div>
        <div className="flex justify-center space-x-6 mt-4">
        <a href="https://github.com/yourprofile" className="text-gray-400 hover:text-white">
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.727-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.757-1.333-1.757-1.087-.743.083-.727.083-.727 1.205.085 1.84 1.238 1.84 1.238 1.07 1.835 2.81 1.305 3.495.998.107-.775.418-1.305.76-1.605-2.665-.305-5.467-1.332-5.467-5.93 0-1.31.467-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23a11.45 11.45 0 013.005-.404c1.02.005 2.045.137 3.005.404 2.28-1.552 3.285-1.23 3.285-1.23.65 1.653.25 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.62-5.475 5.92.435.375.81 1.108.81 2.23 0 1.61-.015 2.91-.015 3.31 0 .315.215.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12" />
            </svg>
          </a>
          <a href="https://linkedin.com/yourprofile" className="text-gray-400 hover:text-white">
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M22.23 0H1.77C.792 0 0 .774 0 1.729v20.543C0 23.227.792 24 1.77 24h20.46C23.208 24 24 23.227 24 22.272V1.729C24 .774 23.208 0 22.23 0zM7.076 20.452H3.797V9.042h3.279v11.41zM5.438 7.721c-1.056 0-1.914-.869-1.914-1.939 0-1.071.858-1.939 1.914-1.939 1.055 0 1.913.868 1.913 1.939 0 1.07-.858 1.939-1.913 1.939zM20.452 20.452h-3.279v-5.746c0-1.371-.025-3.135-1.911-3.135-1.91 0-2.203 1.49-2.203 3.027v5.854H9.78V9.042h3.148v1.563h.045c.438-.829 1.507-1.703 3.104-1.703 3.319 0 3.929 2.187 3.929 5.032v6.518z" />
            </svg>
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;


