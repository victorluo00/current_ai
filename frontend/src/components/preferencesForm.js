import React, { useState } from 'react';

function PreferencesForm({ data }) {
  const [topics, setTopics] = useState('');
  const [summary, setSummary] = useState('');

  const handleTopicsChange = (e) => {
    setTopics(e.target.value);
  };

  async function generateTopArticles(topics) {
    const response = await fetch(
      `http://localhost:8000/recommend_top_articles/${topics}/`
    );
    const data = await response.body;
    // convert readable stream to string
    let stream = await new Response(data);
    let text = await stream.text();
    const summaries = JSON.parse(text).summaries;
    return summaries;
  }

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    let response = await generateTopArticles(topics);
    console.log('summary text', response);
    setSummary(response);
  };

  return (
    <div>
      <h1>Preferences Form</h1>
      <form onSubmit={handleFormSubmit}>
        <label htmlFor="topics">Enter your topics separated by commas:</label>
        <input
          id="topics"
          type="text"
          value={topics}
          onChange={handleTopicsChange}
        ></input>
        <button type="submit">Submit</button>
      </form>
      {summary && (
        <div>
          <h2>Summary:</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default PreferencesForm;
