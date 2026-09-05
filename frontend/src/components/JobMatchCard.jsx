import { useState } from "react";

import api from "../services/api";

function JobMatchCard({ resumeSkills, resumeData }) {
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [detectedSkills, setDetectedSkills] = useState([]);
  const [roleAnalysis, setRoleAnalysis] = useState(null);

  const handleMatch = async () => {
    if (!jobDescription.trim()) {
      alert("Please paste the job description.");
      return;
    }

    if (!resumeSkills?.length) {
      alert("Please analyze your resume first.");
      return;
    }

    try {
      setLoading(true);
      setResult(null);
      setRoleAnalysis(null);

      const response = await api.post(
        "/match-job-description",
        {
          resume_skills: resumeSkills,
          resume_data: resumeData,
          job_description: jobDescription,
        }
      );

      setDetectedSkills(
        response.data.job_description_skills || []
      );

      setResult(
        response.data.job_match_result
      );

      setRoleAnalysis(
        response.data.role_analysis || null
      );

    } catch (error) {
      console.error("Job Match Error:", error);

      if (error.response) {
        alert(
          error.response.data.detail ||
            "Unable to calculate job match."
        );
      } else {
        alert(error.message);
      }

    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="
        bg-white dark:bg-gray-900
        text-gray-800 dark:text-gray-100
        rounded-2xl shadow-lg
        p-8 mt-10 max-w-4xl mx-auto
        transition-colors duration-300
      "
    >

      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">
          🎯 Job Description Match
        </h2>

        <p className="text-gray-500 dark:text-gray-400 mt-2">
          Paste a complete job description to see how well
          your resume matches the role.
        </p>
      </div>

      {/* Resume Skills */}
      <div className="mt-6">
        <h3 className="font-semibold text-gray-700 dark:text-gray-300 mb-3">
          Your Resume Skills
        </h3>

        <div className="flex flex-wrap gap-2">
          {resumeSkills?.length > 0 ? (
            resumeSkills.map((skill, index) => (
              <span
                key={index}
                className="
                  bg-blue-100 dark:bg-blue-900/40
                  text-blue-700 dark:text-blue-300
                  px-3 py-1 rounded-full text-sm
                "
              >
                {skill}
              </span>
            ))
          ) : (
            <p className="text-gray-500 dark:text-gray-400">
              Analyze a resume first.
            </p>
          )}
        </div>
      </div>

      {/* Job Description */}
      <div className="mt-8">
        <label className="block font-semibold text-gray-700 dark:text-gray-300 mb-3">
          Job Description
        </label>

        <textarea
          value={jobDescription}
          onChange={(e) =>
            setJobDescription(e.target.value)
          }
          placeholder={
            "Paste the complete job description here...\n\n" +
            "Example:\n" +
            "We are looking for a Software Engineer with " +
            "experience in Python, React, FastAPI, Docker and AWS..."
          }
          rows={10}
          className="
            w-full
            bg-white dark:bg-gray-800
            text-gray-800 dark:text-gray-100
            placeholder-gray-400 dark:placeholder-gray-500
            border border-gray-300 dark:border-gray-600
            rounded-xl p-4
            focus:outline-none
            focus:ring-2 focus:ring-blue-500
            resize-y
            transition-colors duration-300
          "
        />

        <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">
          Paste the complete job posting. The system will
          automatically identify relevant technical skills.
        </p>
      </div>

      {/* Analyze Button */}
      <button
        onClick={handleMatch}
        disabled={loading || !resumeSkills?.length}
        className="
          w-full mt-6
          bg-blue-600 hover:bg-blue-700
          text-white
          py-3 rounded-xl
          font-semibold
          disabled:bg-gray-400
          transition
        "
      >
        {loading
          ? "Analyzing Job Description..."
          : "Analyze Job Match"}
      </button>

      {/* Results */}
      {result && (
        <div className="mt-10">

          {/* Match Percentage */}
          <div className="text-center">
            <p className="text-sm uppercase tracking-wider text-gray-500 dark:text-gray-400 font-semibold">
              Job Match Score
            </p>

            <p className="text-6xl font-bold text-blue-600 dark:text-blue-400 mt-2">
              {result.match_percentage}%
            </p>

            <p className="text-gray-500 dark:text-gray-400 mt-2">
              {result.matched_count} of{" "}
              {result.total_jd_skills} detected job skills
              matched
            </p>
          </div>

          {/* Detected JD Skills */}
          <div className="mt-10">
            <h3 className="text-lg font-bold text-gray-800 dark:text-gray-100 mb-3">
              🔎 Detected Job Skills
            </h3>

            <div className="flex flex-wrap gap-2">
              {detectedSkills.length > 0 ? (
                detectedSkills.map((skill, index) => (
                  <span
                    key={index}
                    className="
                      bg-purple-100 dark:bg-purple-900/40
                      text-purple-700 dark:text-purple-300
                      px-3 py-1 rounded-full text-sm
                    "
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-gray-500 dark:text-gray-400">
                  No technical skills were detected.
                </p>
              )}
            </div>
          </div>

          {/* Matched Skills */}
          <div className="mt-8">
            <h3 className="text-lg font-bold text-green-700 dark:text-green-400 mb-3">
              ✓ Matched Skills
            </h3>

            <div className="flex flex-wrap gap-2">
              {result.matched_skills.length > 0 ? (
                result.matched_skills.map((skill, index) => (
                  <span
                    key={index}
                    className="
                      bg-green-100 dark:bg-green-900/40
                      text-green-700 dark:text-green-300
                      px-3 py-1 rounded-full text-sm font-medium
                    "
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-gray-500 dark:text-gray-400">
                  No matching skills found.
                </p>
              )}
            </div>
          </div>

          {/* Missing Skills */}
          <div className="mt-8">
            <h3 className="text-lg font-bold text-red-700 dark:text-red-400 mb-3">
              ✗ Missing Skills
            </h3>

            <div className="flex flex-wrap gap-2">
              {result.missing_skills.length > 0 ? (
                result.missing_skills.map((skill, index) => (
                  <span
                    key={index}
                    className="
                      bg-red-100 dark:bg-red-900/40
                      text-red-700 dark:text-red-300
                      px-3 py-1 rounded-full text-sm font-medium
                    "
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-green-600 dark:text-green-400 font-medium">
                  No required skills are missing.
                </p>
              )}
            </div>
          </div>

          {/* Additional Resume Skills */}
          <div className="mt-8">
            <h3 className="text-lg font-bold text-gray-700 dark:text-gray-300 mb-3">
              + Additional Resume Skills
            </h3>

            <div className="flex flex-wrap gap-2">
              {result.additional_resume_skills.length > 0 ? (
                result.additional_resume_skills.map(
                  (skill, index) => (
                    <span
                      key={index}
                      className="
                        bg-gray-100 dark:bg-gray-800
                        text-gray-700 dark:text-gray-300
                        px-3 py-1 rounded-full text-sm
                      "
                    >
                      {skill}
                    </span>
                  )
                )
              ) : (
                <p className="text-gray-500 dark:text-gray-400">
                  No additional skills detected.
                </p>
              )}
            </div>
          </div>

          {/* ================================================= */}
          {/* ROLE-SPECIFIC RESUME ANALYSIS */}
          {/* ================================================= */}

          {roleAnalysis && (
            <div className="mt-12 border-t border-gray-200 dark:border-gray-700 pt-10">

              <h3 className="text-2xl font-bold text-gray-800 dark:text-gray-100 mb-3">
                🎯 Role-Specific Resume Analysis
              </h3>

              <p className="text-gray-500 dark:text-gray-400 mb-6">
                Recommendations based on your resume and the
                specific job description you provided.
              </p>

              {/* Role Fit Summary */}
              {roleAnalysis.role_fit_summary && (
                <div
                  className="
                    bg-blue-50 dark:bg-blue-900/20
                    border border-blue-200 dark:border-blue-700
                    rounded-xl p-5
                  "
                >
                  <h4 className="font-bold text-blue-800 dark:text-blue-300 mb-2">
                    Role Fit Summary
                  </h4>

                  <p className="text-gray-700 dark:text-gray-200 leading-relaxed">
                    {roleAnalysis.role_fit_summary}
                  </p>
                </div>
              )}

              {/* Strong Matches */}
              <div className="mt-7">
                <h4 className="text-lg font-bold text-green-700 dark:text-green-400 mb-3">
                  ✓ Strong Matches
                </h4>

                {roleAnalysis.strong_matches?.length > 0 ? (
                  <ul className="space-y-3">
                    {roleAnalysis.strong_matches.map(
                      (item, index) => (
                        <li
                          key={index}
                          className="
                            bg-green-50 dark:bg-green-900/20
                            border border-green-200 dark:border-green-700
                            rounded-lg p-4
                            text-gray-700 dark:text-gray-200
                          "
                        >
                          {item}
                        </li>
                      )
                    )}
                  </ul>
                ) : (
                  <p className="text-gray-500 dark:text-gray-400">
                    No strong matches identified.
                  </p>
                )}
              </div>

              {/* Weak / Underrepresented */}
              <div className="mt-7">
                <h4 className="text-lg font-bold text-yellow-700 dark:text-yellow-400 mb-3">
                  ⚠ Weak / Underrepresented
                </h4>

                {roleAnalysis.weak_or_underrepresented?.length > 0 ? (
                  <ul className="space-y-3">
                    {roleAnalysis.weak_or_underrepresented.map(
                      (item, index) => (
                        <li
                          key={index}
                          className="
                            bg-yellow-50 dark:bg-yellow-900/20
                            border border-yellow-200 dark:border-yellow-700
                            rounded-lg p-4
                            text-gray-700 dark:text-gray-200
                          "
                        >
                          {item}
                        </li>
                      )
                    )}
                  </ul>
                ) : (
                  <p className="text-gray-500 dark:text-gray-400">
                    No major underrepresented areas identified.
                  </p>
                )}
              </div>

              {/* Missing Requirements */}
              <div className="mt-7">
                <h4 className="text-lg font-bold text-red-700 dark:text-red-400 mb-3">
                  ✗ Missing Requirements
                </h4>

                {roleAnalysis.missing_requirements?.length > 0 ? (
                  <div className="flex flex-wrap gap-2">
                    {roleAnalysis.missing_requirements.map(
                      (item, index) => (
                        <span
                          key={index}
                          className="
                            bg-red-100 dark:bg-red-900/40
                            text-red-700 dark:text-red-300
                            px-3 py-1 rounded-full text-sm font-medium
                          "
                        >
                          {item}
                        </span>
                      )
                    )}
                  </div>
                ) : (
                  <p className="text-green-600 dark:text-green-400 font-medium">
                    No major missing requirements identified.
                  </p>
                )}
              </div>

              {/* Resume Improvements */}
              <div className="mt-7">
                <h4 className="text-lg font-bold text-blue-700 dark:text-blue-400 mb-3">
                  💡 Resume Improvements
                </h4>

                {roleAnalysis.resume_improvements?.length > 0 ? (
                  <ol className="space-y-3">
                    {roleAnalysis.resume_improvements.map(
                      (item, index) => (
                        <li
                          key={index}
                          className="
                            bg-blue-50 dark:bg-blue-900/20
                            border border-blue-200 dark:border-blue-700
                            rounded-lg p-4
                            text-gray-700 dark:text-gray-200
                          "
                        >
                          <span className="font-bold text-blue-700 dark:text-blue-400 mr-2">
                            {index + 1}.
                          </span>

                          {item}
                        </li>
                      )
                    )}
                  </ol>
                ) : (
                  <p className="text-gray-500 dark:text-gray-400">
                    No specific resume improvements identified.
                  </p>
                )}
              </div>

              {/* Keyword Recommendations */}
              <div className="mt-7">
                <h4 className="text-lg font-bold text-purple-700 dark:text-purple-400 mb-3">
                  🔑 Keyword Recommendations
                </h4>

                {roleAnalysis.keyword_recommendations?.length > 0 ? (
                  <ul className="space-y-3">
                    {roleAnalysis.keyword_recommendations.map(
                      (item, index) => (
                        <li
                          key={index}
                          className="
                            bg-purple-50 dark:bg-purple-900/20
                            border border-purple-200 dark:border-purple-700
                            rounded-lg p-4
                            text-gray-700 dark:text-gray-200
                          "
                        >
                          {item}
                        </li>
                      )
                    )}
                  </ul>
                ) : (
                  <p className="text-gray-500 dark:text-gray-400">
                    No additional keyword recommendations.
                  </p>
                )}
              </div>

              {/* Priority Actions */}
              <div className="mt-7">
                <h4 className="text-lg font-bold text-gray-800 dark:text-gray-100 mb-3">
                  🚀 Priority Actions
                </h4>

                {roleAnalysis.priority_actions?.length > 0 ? (
                  <ol className="space-y-3">
                    {roleAnalysis.priority_actions.map(
                      (item, index) => {
                        const cleanItem = String(item)
                          .replace(/^\s*\d+[.)]\s*/, "")
                          .trim();

                        return (
                          <li
                            key={index}
                            className="
                              bg-gray-50 dark:bg-gray-800
                              border border-gray-200 dark:border-gray-700
                              rounded-lg p-4
                              text-gray-700 dark:text-gray-200
                            "
                          >
                            <span className="font-bold mr-2">
                              {index + 1}.
                            </span>

                            {cleanItem}
                          </li>
                        );
                      }
                    )}
                  </ol>
                ) : (
                  <p className="text-gray-500 dark:text-gray-400">
                    No priority actions identified.
                  </p>
                )}
              </div>

            </div>
          )}

        </div>
      )}

    </div>
  );
}

export default JobMatchCard;