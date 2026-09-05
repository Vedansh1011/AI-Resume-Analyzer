import { useState } from "react";

import api from "../services/api";

function ImproveResumeCard({ resumeData }) {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleImprove = async () => {
    if (!resumeData) {
      alert("Please analyze your resume first.");
      return;
    }

    try {
      setLoading(true);
      setResult(null);

      const response = await api.post(
        "/improve-resume",
        resumeData
      );

      setResult(response.data.improvement);

    } catch (error) {
      console.error("Resume Improvement Error:", error);

      if (error.response) {
        alert(
          error.response.data.detail ||
            "Unable to improve resume."
        );
      } else {
        alert(
          error.message ||
            "Unable to connect to the backend."
        );
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
        p-8 mt-10
        transition-colors duration-300
      "
    >

      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">
          ✨ Resume Improvement
        </h2>

        <p className="text-gray-500 dark:text-gray-400 mt-2">
          Get AI-powered suggestions to improve your resume
          wording, structure, ATS compatibility and
          professional presentation.
        </p>
      </div>


      {/* Button */}
      <button
        onClick={handleImprove}
        disabled={loading}
        className="
          w-full mt-6
          bg-indigo-600 hover:bg-indigo-700
          text-white
          py-3 rounded-xl
          font-semibold
          disabled:bg-gray-400
          transition
        "
      >
        {loading
          ? "Improving Resume..."
          : "✨ Improve My Resume"}
      </button>


      {/* Results */}
      {result && (
        <div className="mt-10">


          {/* ================================================== */}
          {/* Professional Summary */}
          {/* ================================================== */}

          {result.professional_summary && (
            <div className="mb-8">

              <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                📝 Professional Summary
              </h3>

              <div
                className="
                  bg-blue-50 dark:bg-blue-900/20
                  border border-blue-100 dark:border-blue-800
                  rounded-xl p-5 space-y-5
                "
              >

                {result.professional_summary.original && (
                  <div>
                    <p className="font-semibold text-gray-700 dark:text-gray-300 mb-2">
                      Original
                    </p>

                    <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
                      {result.professional_summary.original}
                    </p>
                  </div>
                )}

                {result.professional_summary.improved && (
                  <div>
                    <p className="font-semibold text-blue-700 dark:text-blue-400 mb-2">
                      Improved
                    </p>

                    <p className="text-gray-700 dark:text-gray-200 leading-relaxed">
                      {result.professional_summary.improved}
                    </p>
                  </div>
                )}

              </div>
            </div>
          )}


          {/* ================================================== */}
          {/* Education Improvements */}
          {/* ================================================== */}

          {result.education_improvements?.length > 0 && (
            <div className="mb-8">

              <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                🎓 Education Improvements
              </h3>

              <div className="space-y-4">

                {result.education_improvements.map(
                  (item, index) => (
                    <div
                      key={index}
                      className="
                        bg-gray-50 dark:bg-gray-800
                        border border-gray-200 dark:border-gray-700
                        rounded-xl p-5
                      "
                    >

                      <div className="mb-4">

                        <p className="font-semibold text-gray-700 dark:text-gray-300 mb-2">
                          Original
                        </p>

                        <p className="text-gray-600 dark:text-gray-300">
                          {item.original}
                        </p>

                      </div>


                      <div className="mb-4">

                        <p className="font-semibold text-green-700 dark:text-green-400 mb-2">
                          Improved
                        </p>

                        <p className="text-gray-700 dark:text-gray-200">
                          {item.improved}
                        </p>

                      </div>


                      {item.reason && (
                        <div>

                          <p className="font-semibold text-gray-700 dark:text-gray-300 mb-2">
                            Why?
                          </p>

                          <p className="text-gray-600 dark:text-gray-300">
                            {item.reason}
                          </p>

                        </div>
                      )}

                    </div>
                  )
                )}

              </div>
            </div>
          )}


          {/* ================================================== */}
          {/* Experience Improvements */}
          {/* ================================================== */}

          {result.experience_improvements?.length > 0 && (
            <div className="mb-8">

              <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                💼 Experience Improvements
              </h3>

              <div className="space-y-4">

                {result.experience_improvements.map(
                  (item, index) => (
                    <div
                      key={index}
                      className="
                        bg-gray-50 dark:bg-gray-800
                        border border-gray-200 dark:border-gray-700
                        rounded-xl p-5
                      "
                    >

                      {item.section && (
                        <p className="font-semibold text-gray-800 dark:text-gray-100 mb-4">
                          {item.section}
                        </p>
                      )}


                      <div className="mb-4">

                        <p className="font-semibold text-gray-700 dark:text-gray-300 mb-2">
                          Original
                        </p>

                        <p className="text-gray-600 dark:text-gray-300">
                          {item.original}
                        </p>

                      </div>


                      <div className="mb-4">

                        <p className="font-semibold text-green-700 dark:text-green-400 mb-2">
                          Improved
                        </p>

                        <p className="text-gray-700 dark:text-gray-200">
                          {item.improved}
                        </p>

                      </div>


                      {item.reason && (
                        <div>

                          <p className="font-semibold text-gray-700 dark:text-gray-300 mb-2">
                            Why?
                          </p>

                          <p className="text-gray-600 dark:text-gray-300">
                            {item.reason}
                          </p>

                        </div>
                      )}

                    </div>
                  )
                )}

              </div>
            </div>
          )}


          {/* ================================================== */}
          {/* Project Improvements */}
          {/* ================================================== */}

          {result.project_improvements?.length > 0 && (
            <div className="mb-8">

              <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                🚀 Project Improvements
              </h3>

              <div className="space-y-4">

                {result.project_improvements.map(
                  (item, index) => (
                    <div
                      key={index}
                      className="
                        bg-gray-50 dark:bg-gray-800
                        border border-gray-200 dark:border-gray-700
                        rounded-xl p-5
                      "
                    >

                      {item.project && (
                        <p className="font-semibold text-gray-800 dark:text-gray-100 mb-4">
                          {item.project}
                        </p>
                      )}


                      <div className="mb-4">

                        <p className="font-semibold text-gray-700 dark:text-gray-300 mb-2">
                          Original
                        </p>

                        <p className="text-gray-600 dark:text-gray-300">
                          {item.original}
                        </p>

                      </div>


                      <div className="mb-4">

                        <p className="font-semibold text-green-700 dark:text-green-400 mb-2">
                          Improved
                        </p>

                        <p className="text-gray-700 dark:text-gray-200">
                          {item.improved}
                        </p>

                      </div>


                      {item.reason && (
                        <div>

                          <p className="font-semibold text-gray-700 dark:text-gray-300 mb-2">
                            Why?
                          </p>

                          <p className="text-gray-600 dark:text-gray-300">
                            {item.reason}
                          </p>

                        </div>
                      )}

                    </div>
                  )
                )}

              </div>
            </div>
          )}


          {/* ================================================== */}
          {/* Skills Improvements */}
          {/* ================================================== */}

          {result.skills_improvements && (
            <div className="mb-8">

              <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                🛠️ Skills Improvements
              </h3>

              <div
                className="
                  bg-gray-50 dark:bg-gray-800
                  border border-gray-200 dark:border-gray-700
                  rounded-xl p-5
                "
              >

                {/* Duplicates */}
                {result.skills_improvements
                  .duplicates_to_remove?.length > 0 && (

                  <div className="mb-5">

                    <p className="font-semibold text-gray-700 dark:text-gray-300">
                      Duplicates to Remove
                    </p>

                    <div className="flex flex-wrap gap-2 mt-3">

                      {result.skills_improvements
                        .duplicates_to_remove
                        .map((skill, index) => (

                          <span
                            key={index}
                            className="
                              bg-red-100 dark:bg-red-900/40
                              text-red-700 dark:text-red-300
                              px-3 py-1 rounded-full text-sm
                            "
                          >
                            {skill}
                          </span>

                        ))}

                    </div>
                  </div>
                )}


                {/* Recommended Structure */}
                {result.skills_improvements
                  .recommended_structure && (

                  <div>

                    <p className="font-semibold text-gray-700 dark:text-gray-300">
                      Recommended Skills Structure
                    </p>

                    <div className="mt-4 space-y-4">

                      {Object.entries(
                        result.skills_improvements
                          .recommended_structure
                      ).map(([category, values]) => (

                        <div key={category}>

                          <p className="font-medium text-gray-800 dark:text-gray-100">
                            {category}
                          </p>

                          <div className="flex flex-wrap gap-2 mt-2">

                            {Array.isArray(values) &&
                              values.map(
                                (value, index) => (

                                  <span
                                    key={index}
                                    className="
                                      bg-blue-100 dark:bg-blue-900/40
                                      text-blue-700 dark:text-blue-300
                                      px-3 py-1 rounded-full text-sm
                                    "
                                  >
                                    {value}
                                  </span>

                                )
                              )}

                          </div>
                        </div>

                      ))}

                    </div>
                  </div>
                )}


                {/* Notes */}
                {result.skills_improvements.notes?.length > 0 && (

                  <div className="mt-5">

                    <p className="font-semibold text-gray-700 dark:text-gray-300">
                      Notes
                    </p>

                    <ul className="list-disc list-inside mt-2 text-gray-600 dark:text-gray-300">

                      {result.skills_improvements.notes.map(
                        (note, index) => (

                          <li key={index}>
                            {note}
                          </li>

                        )
                      )}

                    </ul>

                  </div>
                )}

              </div>
            </div>
          )}


          {/* ================================================== */}
          {/* Readability Improvements */}
          {/* ================================================== */}

          {result.readability_improvements?.length > 0 && (

            <div className="mb-8">

              <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                📖 Readability Improvements
              </h3>

              <div
                className="
                  bg-yellow-50 dark:bg-yellow-900/20
                  border border-yellow-100 dark:border-yellow-800
                  rounded-xl p-5
                "
              >

                <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-200">

                  {result.readability_improvements.map(
                    (item, index) => (

                      <li key={index}>
                        {item}
                      </li>

                    )
                  )}

                </ul>

              </div>
            </div>
          )}


          {/* ================================================== */}
          {/* ATS Improvements */}
          {/* ================================================== */}

          {result.ats_improvements?.length > 0 && (

            <div className="mb-8">

              <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                📊 ATS Improvements
              </h3>

              <div
                className="
                  bg-purple-50 dark:bg-purple-900/20
                  border border-purple-100 dark:border-purple-800
                  rounded-xl p-5
                "
              >

                <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-200">

                  {result.ats_improvements.map(
                    (item, index) => (

                      <li key={index}>
                        {item}
                      </li>

                    )
                  )}

                </ul>

              </div>
            </div>
          )}


          {/* ================================================== */}
          {/* Important Notes */}
          {/* ================================================== */}

          {result.important_notes?.length > 0 && (

            <div>

              <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                ⚠️ Important Notes
              </h3>

              <div
                className="
                  bg-orange-50 dark:bg-orange-900/20
                  border border-orange-100 dark:border-orange-800
                  rounded-xl p-5
                "
              >

                <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-200">

                  {result.important_notes.map(
                    (item, index) => (

                      <li key={index}>
                        {item}
                      </li>

                    )
                  )}

                </ul>

              </div>
            </div>
          )}

        </div>
      )}
    </div>
  );
}

export default ImproveResumeCard;