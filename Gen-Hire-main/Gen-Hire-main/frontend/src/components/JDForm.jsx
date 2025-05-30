import React, { useState } from "react";
import api from "../api";

const JDForm = ({ setMatchData }) => {
  const [jdText, setJdText] = useState("");
  const [threshold, setThreshold] = useState(80); // default 80%
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!jdText.trim()) return;

    try {
      setLoading(true);
      const response = await api.post("/match", {
        jd_text: jdText,
        threshold: parseFloat(threshold),
      });

      setMatchData(response.data.data);
    } catch (err) {
      console.error("Matching failed:", err);
      alert("Error occurred while matching!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.box}>
      <h2>🔍 Enter Job Description</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          rows={10}
          cols={80}
          placeholder="Paste job description here..."
          value={jdText}
          onChange={(e) => setJdText(e.target.value)}
          required
        />
        <br />
        <label>
          Matching Threshold (%):{" "}
          <input
            type="number"
            value={threshold}
            onChange={(e) => setThreshold(e.target.value)}
            min="0"
            max="100"
            step="1"
          />
        </label>
        <br />
        <button type="submit" disabled={loading}>
          {loading ? "Matching..." : "Match Candidates"}
        </button>
      </form>
    </div>
  );
};

const styles = {
  box: {
    border: "1px solid #ccc",
    padding: "1rem",
    borderRadius: "8px",
    marginBottom: "2rem",
  },
};

export default JDForm;
