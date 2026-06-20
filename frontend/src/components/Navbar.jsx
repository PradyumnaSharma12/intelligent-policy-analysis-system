import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="w-full bg-white border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-8 py-4 flex justify-between items-center">
        <h1 className="text-xl font-bold text-blue-600">
          PolicyAI
        </h1>

        <div className="flex gap-6">
          <a href="#features">Features</a>
          <a href="#how">How It Works</a>

          <Link
            to="/dashboard"
            className="bg-blue-600 text-white px-4 py-2 rounded-lg"
          >
            Dashboard
          </Link>
        </div>
      </div>
    </nav>
  );
}