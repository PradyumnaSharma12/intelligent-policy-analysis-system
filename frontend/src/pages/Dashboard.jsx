import { useState } from "react";
import Sidebar from "../components/Sidebar";
import UploadZone from "../components/UploadZone";
import AnalysisCards from "../components/AnalysisCards";
import RecommendationPanel from "../components/RecommendationPanel";
import PolicyAnalysisPanel from "../components/PolicyAnalysisPanel";
import SummaryPanel from "../components/SummaryPanel";
import ChatBox from "../components/ChatBox";

export default function Dashboard() {
  const [policyData, setPolicyData] = useState(null);
  const [summary, setSummary] = useState("");

  return (
    <div className="flex bg-[#F8F9FB] min-h-screen">
      <Sidebar />

      <div className="flex-1 p-8 space-y-8">
        <UploadZone
          policyData={policyData}
          setPolicyData={setPolicyData}
          setSummary={setSummary}
        />

        <AnalysisCards policyData={policyData} />

        <SummaryPanel summary={summary} />

        <div className="grid lg:grid-cols-2 gap-8">
          <PolicyAnalysisPanel policyData={policyData} />
          <RecommendationPanel policyData={policyData} />
        </div>

        <ChatBox />
      </div>
    </div>
  );
}