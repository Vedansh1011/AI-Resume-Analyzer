import { useState } from "react";

import api from "../services/api";

function UploadCard({ setResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleAnalyze = async () => {
    if (!file) {
      alert("Please select a PDF resume.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await api.post(
        "/analyze-resume",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error("Full Error:", error);

      if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Data:", error.response.data);

        alert(
          error.response.data.detail || "Backend Error"
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
        p-8 mt-12 max-w-2xl mx-auto
        transition-colors duration-300
      "
    >
      <h2 className="text-2xl font-bold text-center mb-6">
        📄 Upload Your Resume
      </h2>

      <label
        className="
          border-2 border-dashed border-blue-400
          dark:border-blue-500
          rounded-xl
          h-52 flex flex-col justify-center items-center
          cursor-pointer
          hover:bg-blue-50 dark:hover:bg-gray-800
          transition
        "
      >
        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          className="hidden"
        />

        <p className="text-5xl">📄</p>

        <p className="mt-3 text-lg font-semibold">
          Click to upload your PDF
        </p>

        <p className="text-gray-500 dark:text-gray-400 mt-2">
          Only PDF resumes are supported
        </p>
      </label>

      {file && (
        <p className="mt-5 text-center text-green-600 dark:text-green-400 font-medium">
          Selected: {file.name}
        </p>
      )}

      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="
          w-full mt-8
          bg-blue-600 hover:bg-blue-700
          text-white
          py-3 rounded-xl
          text-lg font-semibold
          disabled:bg-gray-400
          transition
        "
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>
    </div>
  );
}

export default UploadCard;