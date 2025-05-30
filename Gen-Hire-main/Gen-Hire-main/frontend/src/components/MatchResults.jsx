import React from "react";

const MatchResults = ({ data }) => {
  if (!data || data.length === 0) {
    return (
      <div style={styles.box}>
        <h2>🎯 Match Results</h2>
        <p>No candidates matched yet. Submit a JD to begin.</p>
      </div>
    );
  }

  return (
    <div style={styles.box}>
      <h2>🎯 Match Results</h2>
      <table style={styles.table}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Match %</th>
            <th>Experience</th>
            <th>Skills</th>
            <th>Certifications</th>
          </tr>
        </thead>
        <tbody>
          {data.map((candidate, idx) => (
            <tr key={idx}>
              <td>{candidate.name}</td>
              <td>{candidate.match_score}%</td>
              <td>{candidate.experience || "N/A"}</td>
              <td>{(candidate.skills || []).join(", ")}</td>
              <td>{(candidate.certifications || []).join(", ")}</td>
            </tr>
          ))}
        </tbody>
      </table>
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
  table: {
    width: "100%",
    borderCollapse: "collapse",
  },
  th: {
    background: "#eee",
    padding: "8px",
  },
  td: {
    padding: "8px",
    borderBottom: "1px solid #ddd",
  },
};

export default MatchResults;
