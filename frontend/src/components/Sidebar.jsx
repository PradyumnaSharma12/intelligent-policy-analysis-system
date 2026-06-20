import {
  LayoutDashboard,
  FileText,
  History,
  Settings,
} from "lucide-react";

export default function Sidebar() {
  const menu = [
    { icon: <LayoutDashboard size={20} />, text: "Dashboard" },
    { icon: <FileText size={20} />, text: "Policies" },
    { icon: <History size={20} />, text: "History" },
    { icon: <Settings size={20} />, text: "Settings" },
  ];

  return (
    <div className="w-64 bg-white border-r border-gray-200 h-screen p-5">
      <h1 className="text-2xl font-bold text-blue-600 mb-10">
        PolicyAI
      </h1>

      <div className="space-y-3">
        {menu.map((item) => (
          <div
            key={item.text}
            className="flex items-center gap-3 p-3 rounded-lg hover:bg-gray-100 cursor-pointer"
          >
            {item.icon}
            {item.text}
          </div>
        ))}
      </div>
    </div>
  );
}