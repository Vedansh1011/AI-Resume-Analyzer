import { useState } from "react";

import Navbar from "../components/Navbar";
import UploadCard from "../components/UploadCard";
import ATSCard from "../components/ATSCard";
import AIReviewCard from "../components/AIReviewCard";
import JobMatchCard from "../components/JobMatchCard";
import ImproveResumeCard from "../components/ImproveResumeCard";


function Home() {
  const [result, setResult] = useState(null);

  // ATS is the first section shown after resume analysis
  const [activeTab, setActiveTab] = useState("ats");


  const handleNewResume = () => {
    setResult(null);
    setActiveTab("ats");
  };


  return (
    <div className="min-h-screen bg-slate-100 dark:bg-gray-950 transition-colors duration-300">

      {/* ================================================= */}
      {/* NAVBAR */}
      {/* ================================================= */}

      <Navbar
        activeTab={activeTab}
        onTabChange={setActiveTab}
        hasResult={!!result}
        onNewResume={handleNewResume}
      />


      {/* ================================================= */}
      {/* MAIN CONTENT */}
      {/* ================================================= */}

      <main className="max-w-6xl mx-auto px-4 sm:px-6 py-10">


        {/* ================================================= */}
        {/* UPLOAD SCREEN */}
        {/* ================================================= */}

        {!result && (
          <>

            <div className="text-center mb-10">

              <h1 className="text-4xl md:text-5xl font-bold text-gray-800 dark:text-white">
                Analyze Your Resume
              </h1>

              <p className="text-gray-600 dark:text-gray-300 mt-4 text-lg max-w-3xl mx-auto">
                Upload your resume to analyze its ATS compatibility,
                get AI-powered feedback, match it with job descriptions,
                and receive improvement suggestions.
              </p>

            </div>


            <UploadCard
              setResult={setResult}
            />

          </>
        )}


        {/* ================================================= */}
        {/* ATS SCORE */}
        {/* ================================================= */}

        {result && activeTab === "ats" && (
          <ATSCard
            ats={result.ats_result}
          />
        )}


        {/* ================================================= */}
        {/* AI REVIEW */}
        {/* ================================================= */}

        {result && activeTab === "ai" && (
          <AIReviewCard
            review={result.ai_review}
          />
        )}


        {/* ================================================= */}
        {/* JOB MATCH */}
        {/* ================================================= */}

        {result && activeTab === "job" && (
          <JobMatchCard
            resumeSkills={result.resume_info.skills}
            resumeData={result.resume_info}
          />
        )}


        {/* ================================================= */}
        {/* IMPROVE RESUME */}
        {/* ================================================= */}

        {result && activeTab === "improve" && (
          <ImproveResumeCard
            resumeData={result.resume_info}
          />
        )}

      </main>

    </div>
  );
}


export default Home;