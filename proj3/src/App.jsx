import { useState } from 'react'
import logo from './assets/Star-Wars-Logo-1.png'
import './App.css'

import Form from "./components/Form.jsx"

function App() {

  return (
    <>
      <div>
        <a target="_blank">
          <img src={logo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h2>Empire or Resistance Prediction Model</h2>
      <p className="read-the-docs">
        Fill out the form and hit submit to make a prediction
      </p>
      <div className="card">
        <Form />
      </div>
    </>
  )
}

export default App
