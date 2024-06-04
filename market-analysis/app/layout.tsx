"use client";

import { ReactNode } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import '../styles/globals.css';
import useSmoothScroll from './components/hooks/useSmoothScroll';

export default function RootLayout({ children }: { children: ReactNode }) {
  useSmoothScroll();

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

