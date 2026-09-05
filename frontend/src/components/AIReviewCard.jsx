function AIReviewCard({ review }) {
  if (!review) {
    return null;
  }

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
      <div className="flex items-center gap-3 mb-8">
        <div className="text-3xl">
          🤖
        </div>

        <div>
          <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">
            AI Resume Review
          </h2>

          <p className="text-gray-500 dark:text-gray-400">
            Detailed analysis and actionable recommendations
          </p>
        </div>
      </div>


      {/* ===================================================== */}
      {/* STRENGTHS */}
      {/* ===================================================== */}

      {review.strengths?.length > 0 && (
        <section className="mb-8">

          <h3 className="text-xl font-bold text-green-700 dark:text-green-400 mb-4">
            ✓ Strengths
          </h3>

          <div className="space-y-3">
            {review.strengths.map((strength, index) => (
              <div
                key={index}
                className="
                  bg-green-50 dark:bg-green-900/20
                  border border-green-200 dark:border-green-700
                  rounded-xl p-4
                  text-gray-700 dark:text-gray-200
                  leading-relaxed
                  transition-colors duration-300
                "
              >
                {strength}
              </div>
            ))}
          </div>

        </section>
      )}


      {/* ===================================================== */}
      {/* WEAKNESSES */}
      {/* ===================================================== */}

      {review.weaknesses?.length > 0 && (
        <section className="mb-8">

          <h3 className="text-xl font-bold text-red-700 dark:text-red-400 mb-4">
            ⚠ Weaknesses
          </h3>

          <div className="space-y-3">
            {review.weaknesses.map((weakness, index) => (
              <div
                key={index}
                className="
                  bg-red-50 dark:bg-red-900/20
                  border border-red-200 dark:border-red-700
                  rounded-xl p-4
                  text-gray-700 dark:text-gray-200
                  leading-relaxed
                  transition-colors duration-300
                "
              >
                {weakness}
              </div>
            ))}
          </div>

        </section>
      )}


      {/* ===================================================== */}
      {/* KEYWORD ANALYSIS */}
      {/* ===================================================== */}

      {review.keyword_analysis && (
        <section className="mb-8">

          <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-5">
            🔍 Keyword Analysis
          </h3>

          <div className="grid md:grid-cols-2 gap-5">

            {/* Duplicates */}
            <KeywordBox
              title="Duplicate Skills"
              items={review.keyword_analysis.duplicates}
              color="red"
              emptyText="No duplicate skills detected."
            />

            {/* Overlapping */}
            <KeywordBox
              title="Overlapping Terms"
              items={review.keyword_analysis.overlapping_terms}
              color="amber"
              emptyText="No major overlapping terms detected."
            />

            {/* Inconsistent */}
            <KeywordBox
              title="Inconsistent Terms"
              items={review.keyword_analysis.inconsistent_terms}
              color="yellow"
              emptyText="No major inconsistencies detected."
            />

            {/* Potential */}
            <KeywordBox
              title="Potential Keywords"
              items={review.keyword_analysis.potential_keywords}
              color="blue"
              emptyText="No additional keywords strongly recommended."
            />

          </div>

        </section>
      )}


      {/* ===================================================== */}
      {/* READABILITY */}
      {/* ===================================================== */}

      {review.readability && (
        <section className="mb-8">

          <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-5">
            📖 Readability
          </h3>

          <div className="grid md:grid-cols-2 gap-5">

            <div
              className="
                bg-orange-50 dark:bg-orange-900/20
                border border-orange-200 dark:border-orange-700
                rounded-xl p-5
                transition-colors duration-300
              "
            >

              <h4 className="font-bold text-orange-700 dark:text-orange-400 mb-3">
                Issues
              </h4>

              {review.readability.issues?.length > 0 ? (
                <ul className="space-y-3">
                  {review.readability.issues.map((issue, index) => (
                    <li
                      key={index}
                      className="text-gray-700 dark:text-gray-200 leading-relaxed"
                    >
                      • {issue}
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-gray-500 dark:text-gray-400">
                  No major readability issues detected.
                </p>
              )}

            </div>


            <div
              className="
                bg-blue-50 dark:bg-blue-900/20
                border border-blue-200 dark:border-blue-700
                rounded-xl p-5
                transition-colors duration-300
              "
            >

              <h4 className="font-bold text-blue-700 dark:text-blue-400 mb-3">
                Improvements
              </h4>

              {review.readability.improvements?.length > 0 ? (
                <ul className="space-y-3">
                  {review.readability.improvements.map(
                    (improvement, index) => (
                      <li
                        key={index}
                        className="text-gray-700 dark:text-gray-200 leading-relaxed"
                      >
                        • {improvement}
                      </li>
                    )
                  )}
                </ul>
              ) : (
                <p className="text-gray-500 dark:text-gray-400">
                  No specific readability improvements detected.
                </p>
              )}

            </div>

          </div>

        </section>
      )}


      {/* ===================================================== */}
      {/* BULLET IMPROVEMENTS */}
      {/* ===================================================== */}

      {review.bullet_improvements?.length > 0 && (
        <section className="mb-8">

          <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-5">
            ✏️ Bullet Improvements
          </h3>

          <div className="space-y-6">

            {review.bullet_improvements.map((item, index) => (
              <div
                key={index}
                className="
                  border border-gray-200 dark:border-gray-700
                  rounded-xl overflow-hidden
                  transition-colors duration-300
                "
              >

                {/* Section */}
                <div
                  className="
                    bg-gray-50 dark:bg-gray-800
                    px-5 py-3
                    border-b border-gray-200 dark:border-gray-700
                  "
                >
                  <p className="font-bold text-gray-800 dark:text-gray-100">
                    {item.section}
                  </p>

                  <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
                    {item.issue}
                  </p>
                </div>


                {/* Before */}
                <div className="p-5">

                  <p className="text-sm font-bold text-red-600 dark:text-red-400 mb-2">
                    BEFORE
                  </p>

                  <div
                    className="
                      bg-red-50 dark:bg-red-900/20
                      border border-red-100 dark:border-red-800
                      rounded-lg p-4
                      text-gray-700 dark:text-gray-200
                    "
                  >
                    {item.before}
                  </div>

                </div>


                {/* After */}
                <div className="px-5 pb-5">

                  <p className="text-sm font-bold text-green-600 dark:text-green-400 mb-2">
                    AFTER
                  </p>

                  <div
                    className="
                      bg-green-50 dark:bg-green-900/20
                      border border-green-100 dark:border-green-800
                      rounded-lg p-4
                      text-gray-700 dark:text-gray-200
                    "
                  >
                    {item.after}
                  </div>

                </div>

              </div>
            ))}

          </div>

        </section>
      )}


      {/* ===================================================== */}
      {/* SUGGESTIONS */}
      {/* ===================================================== */}

      {review.suggestions?.length > 0 && (
        <section className="mb-8">

          <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
            💡 Actionable Improvements
          </h3>

          <div className="space-y-3">

            {review.suggestions.map((suggestion, index) => (
              <div
                key={index}
                className="
                  bg-blue-50 dark:bg-blue-900/20
                  border border-blue-200 dark:border-blue-700
                  rounded-xl p-4
                  text-gray-700 dark:text-gray-200
                  leading-relaxed
                  transition-colors duration-300
                "
              >
                <span className="font-bold text-blue-600 dark:text-blue-400">
                  {index + 1}.
                </span>{" "}
                {suggestion}
              </div>
            ))}

          </div>

        </section>
      )}


      {/* ===================================================== */}
      {/* OVERALL REVIEW */}
      {/* ===================================================== */}

      {review.overall_review && (
        <section>

          <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100 mb-4">
            📝 Overall Review
          </h3>

          <div
            className="
              bg-slate-50 dark:bg-gray-800
              border border-slate-200 dark:border-gray-700
              rounded-xl p-6
              transition-colors duration-300
            "
          >

            <p className="text-gray-700 dark:text-gray-200 leading-relaxed">
              {review.overall_review}
            </p>

          </div>

        </section>
      )}

    </div>
  );
}


/* ========================================================= */
/* KEYWORD BOX COMPONENT */
/* ========================================================= */

function KeywordBox({
  title,
  items,
  color,
  emptyText
}) {

  const colorClasses = {
    red: `
      bg-red-50 dark:bg-red-900/20
      border-red-200 dark:border-red-700
      text-red-700 dark:text-red-400
    `,

    amber: `
      bg-amber-50 dark:bg-amber-900/20
      border-amber-200 dark:border-amber-700
      text-amber-700 dark:text-amber-400
    `,

    yellow: `
      bg-yellow-50 dark:bg-yellow-900/20
      border-yellow-200 dark:border-yellow-700
      text-yellow-700 dark:text-yellow-400
    `,

    blue: `
      bg-blue-50 dark:bg-blue-900/20
      border-blue-200 dark:border-blue-700
      text-blue-700 dark:text-blue-400
    `
  };

  const classes =
    colorClasses[color] ||
    colorClasses.blue;

  return (
    <div
      className={`
        border rounded-xl p-5
        transition-colors duration-300
        ${classes}
      `}
    >

      <h4 className="font-bold mb-3">
        {title}
      </h4>

      {items?.length > 0 ? (

        <div className="flex flex-wrap gap-2">

          {items.map((item, index) => (
            <span
              key={index}
              className="
                bg-white/70 dark:bg-gray-800/70
                border border-current
                px-3 py-1 rounded-full text-sm
              "
            >
              {item}
            </span>
          ))}

        </div>

      ) : (

        <p className="text-sm opacity-80">
          {emptyText}
        </p>

      )}

    </div>
  );
}


export default AIReviewCard;