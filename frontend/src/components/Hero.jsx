import { Link } from "react-router-dom";

export default function Hero() {
  return (
    <section className="max-w-7xl mx-auto px-8 py-24 text-center">
      <h1 className="text-6xl font-bold text-gray-900 mb-6">
        Intelligent AI-Based
        <span className="text-blue-600"> Policy Analysis</span>
      </h1>

      <p className="text-xl text-gray-600 max-w-3xl mx-auto mb-10">
        Upload policies, generate summaries,
        classify documents, retrieve insights,
        and receive AI-powered recommendations.
      </p>

      <Link
        to="/dashboard"
        className="bg-blue-600 text-white px-8 py-4 rounded-xl text-lg"
      >
        Get Started
      </Link>
    </section>
  );
}