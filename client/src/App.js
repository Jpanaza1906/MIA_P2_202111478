import React from 'react'
import './App.css'

//Componentes
import Header from './Header'
import Main from './Main'
import Footer from './Footer'

//Estilos de boostrap
import 'bootstrap/dist/css/bootstrap.min.css'


function App() {

  return (
    <div className='App'>
      <Header/>
      <Main/>
      <Footer/>
    </div>
  )
}

export default App
