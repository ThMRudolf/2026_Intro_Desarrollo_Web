import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import {ProgramasConArreglo} from './Programas.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ProgramasConArreglo />
  </StrictMode>,
)
