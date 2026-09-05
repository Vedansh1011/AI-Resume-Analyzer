function ATSCard({ ats }) {
  const breakdown = ats.breakdown;

  const getRating = (score) => {
    if (score >= 90) return "Excellent";
    if (score >= 80) return "Good";
    if (score >= 70) return "Fair";
    if (score >= 60) return "Needs Improvement";
    return "Weak";
  };

  const rating = getRating(ats.ats_score);

  return (
    <div
      className="
        bg-white dark:bg-gray-900
        text-gray-800 dark:text-gray-100
        rounded-2xl shadow-lg
        p-8 mt-10 max-w-3xl mx-auto
        transition-colors duration-300
      "
    >
      {/* Overall Score */}
      <div className="text-center">
        <p className="text-sm uppercase tracking-wider text-gray-500 dark:text-gray-400 font-semibold">
          ATS Score
        </p>

        <p className="text-7xl font-bold text-blue-600 dark:text-blue-400 mt-3">
          {ats.ats_score}
        </p>

        <p className="text-gray-500 dark:text-gray-400">
          out of {ats.max_score}
        </p>

        <span
          className="
            inline-block mt-4 px-4 py-2 rounded-full
            bg-blue-100 dark:bg-blue-900/40
            text-blue-700 dark:text-blue-300
            font-semibold
          "
        >
          {rating}
        </span>
      </div>

      {/* Breakdown */}
      <div className="mt-10">
        <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-6">
          Score Breakdown
        </h3>

        <div className="space-y-5">
          <ScoreRow
            label="Contact & Header"
            score={breakdown.contact}
            max={10}
          />

          <ScoreRow
            label="Skills & Keywords"
            score={breakdown.skills}
            max={20}
          />

          <ScoreRow
            label="Education"
            score={breakdown.education}
            max={15}
          />

          <ScoreRow
            label="Experience"
            score={breakdown.experience}
            max={20}
          />

          <ScoreRow
            label="Projects"
            score={breakdown.projects}
            max={15}
          />

          <ScoreRow
            label="Content Quality"
            score={breakdown.content_quality}
            max={10}
          />

          <ScoreRow
            label="ATS Structure"
            score={breakdown.ats_structure}
            max={10}
          />
        </div>
      </div>

      {/* Suggestions */}
      {ats.suggestions?.length > 0 && (
        <div className="mt-10">
          <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
            Key Improvements
          </h3>

          <div className="space-y-3">
            {ats.suggestions.map((suggestion, index) => (
              <div
                key={index}
                className="
                  bg-amber-50 dark:bg-amber-900/20
                  border border-amber-200 dark:border-amber-700
                  rounded-xl p-4
                  text-gray-700 dark:text-gray-200
                  transition-colors duration-300
                "
              >
                ⚠️ {suggestion}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function ScoreRow({ label, score, max }) {
  const percentage = (score / max) * 100;

  return (
    <div>
      <div className="flex justify-between items-center mb-2">
        <span className="font-medium text-gray-700 dark:text-gray-300">
          {label}
        </span>

        <span className="font-semibold text-gray-600 dark:text-gray-400">
          {score}/{max}
        </span>
      </div>

      <div className="w-full h-2.5 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
        <div
          className="h-full bg-blue-600 dark:bg-blue-500 rounded-full transition-all duration-700"
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  );
}

export default ATSCard;