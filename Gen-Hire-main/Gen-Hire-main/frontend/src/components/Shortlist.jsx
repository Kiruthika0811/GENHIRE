import React, { useState } from "react";
import api from "../api";

const Shortlist = ({ data, threshold }) => {
  const [mailStatus, setMailStatus] = useState({});

  const handleSendMail = async (candidate) => {
    const key = candidate.name;

    try {
      setMailStatus((prev) => ({ ...prev, [key]: "sending" }));

      await api.post("/send_interview_mail", {
        name: candidate.name,
        email: candidate.email, // Ensure `email` is available in candidate object
        match_score: candidate.match_score,
        job_title: "Software Engineer", // or pass dynamically
      });

      setMailStatus((prev) => ({ ...prev, [key]: "sent" }));
    } catch (err) {
      console.error("Failed to send mail:", err);
      setMailStatus((prev) => ({ ...prev, [key]: "error" }));
    }
  };

  const shortlisted = data.filter((c) => c.match_score >= threshold);

  if (shortlisted.length === 0) {
    return (
      <div style={styles.box}>
        <h2>✅ Shortlisted Candidates</h2>
        <p>No candidates met the threshold of {threshold}%.</p>
      </div>
    );
  }

  return (
    <div style={styles.box}>
      <h2>✅ Shortlisted Candidates</h2>
      <ul>
        {shortlisted.map((c, idx) => (
          <li key={idx} style={{ marginBottom: "1rem" }}>
            <strong>{c.name}</strong> ({c.match_score}% match)
            <br />
            {c.email ? <span>Email: {c.email}</span> : <span style={{ color: "red" }}>No Email</span>}
            <br />
            <button
              onClick={() => handleSendMail(c)}
              disabled={mailStatus[c.name] === "sending" || !c.email}
            >
              {mailStatus[c.name] === "sending"
                ? "Sending..."
                : mailStatus[c.name] === "sent"
                ? "Sent ✔"
                : "📧 Send Mail"}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

const styles = {
  box: {
    border: "1px solid #4caf50",
    padding: "1rem",
    borderRadius: "8px",
    marginTop: "2rem",
    backgroundColor: "#f4fff4",
  },
};

export default Shortlist;
