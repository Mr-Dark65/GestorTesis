import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import {LoginForm} from './components/LoginForm'
import { Prueba } from './components/prueba'
import { Toaster } from 'react-hot-toast'
import { Header } from './components/header'

function App(){
  return(
    <BrowserRouter>
      <Header/>
      <Routes>
        <Route path='/' element={<Navigate to='/login'/>}/>
        <Route path='/login' element={<LoginForm/>}/>
        <Route path='/Prueba' element={<Prueba/>}/>
      </Routes>
      <Toaster/>
    </BrowserRouter>
  )
}

export default App