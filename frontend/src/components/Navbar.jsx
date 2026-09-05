import { useEffect, useState } from "react";

function Navbar({
  activeTab,
  onTabChange,
  hasResult,
  onNewResume,
}) {
  const [darkMode, setDarkMode] = useState(() => {
    return localStorage.getItem("theme") === "dark";
  });

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  }, [darkMode]);

  const tabs = [
    {
      id: "ats",
      label: "ATS Score",
      icon: "📊",
    },
    {
      id: "ai",
      label: "AI Review",
      icon: "🤖",
    },
    {
      id: "job",
      label: "Job Match",
      icon: "🎯",
    },
    {
      id: "improve",
      label: "Improve Resume",
      icon: "✨",
    },
  ];

  return (
    <nav className="bg-white dark:bg-gray-900 shadow-md sticky top-0 z-50 transition-colors duration-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-4">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

          {/* Logo */}
          <button
            onClick={() => {
              if (hasResult) {
                onTabChange("ats");
              }
            }}
            className="text-2xl font-bold text-blue-600 dark:text-blue-400 text-left"
          >
            📄 AI Resume Analyzer
          </button>

          {/* Navigation */}
          <div className="flex flex-wrap gap-2">
            {tabs.map((tab) => {
              const isActive = activeTab === tab.id;

              return (
                <button
                  key={tab.id}
                  onClick={() => onTabChange(tab.id)}
                  disabled={!hasResult}
                  className={`
                    px-4 py-2 rounded-lg font-semibold
                    transition-all duration-200
                    ${
                      isActive
                        ? "bg-blue-600 text-white shadow-md"
                        : !hasResult
                        ? "bg-gray-100 dark:bg-gray-800 text-gray-400 cursor-not-allowed"
                        : "bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-200 hover:bg-blue-100 dark:hover:bg-gray-700 hover:text-blue-700 dark:hover:text-blue-400"
                    }
                  `}
                >
                  <span className="mr-2">
                    {tab.icon}
                  </span>
                  {tab.label}
                </button>
              );
            })}

            {/* New Resume */}
            {hasResult && (
              <button
                onClick={onNewResume}
                className="
                  px-4 py-2 rounded-lg font-semibold
                  bg-gray-800 dark:bg-gray-700 text-white
                  hover:bg-gray-900 dark:hover:bg-gray-600
                  transition-all duration-200
                "
              >
                Upload New Resume
              </button>
            )}

            {/* Theme Toggle */}
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="
                w-10 h-10 rounded-lg
                bg-gray-100 dark:bg-gray-800
                text-gray-700 dark:text-gray-200
                hover:bg-gray-200 dark:hover:bg-gray-700
                transition-all duration-200
                flex items-center justify-center
              "
              title={darkMode ? "Switch to Light Mode" : "Switch to Dark Mode"}
            >
              {darkMode ? "☀️" : "🌙"}
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;