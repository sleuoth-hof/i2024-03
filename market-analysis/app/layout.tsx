import React, { ReactNode } from 'react';
import Navbar from '../app/components/Navbar';
import Footer from '../app/components/Footer';
import '../styles/globals.css'; 

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  );
}
