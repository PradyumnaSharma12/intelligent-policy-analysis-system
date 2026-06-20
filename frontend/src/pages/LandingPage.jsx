import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features";

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-[#F8F9FB]">
      <Navbar />
      <Hero />
      <Features />
    </div>
  );
}