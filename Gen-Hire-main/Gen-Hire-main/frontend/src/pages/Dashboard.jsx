import React, { useState } from "react";
import JDInput from "../components/JDInput";
import MatchResults from "../components/MatchResults";
import Shortlist from "../components/Shortlist";

const Dashboard = () => {
  const [matches, setMatches] = useState([]);
  const [threshold, setThreshold] = useState(80);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>🚀 AI Job Matcher Dashboard</h1>

      <JDInput onMatchComplete={setMatches} />

      {matches.length > 0 && (
        <>
          <MatchResults data={matches} />
          <Shortlist data={matches} threshold={threshold} />
        </>
      )}
    </div>
  );
};

export default Dashboard;
