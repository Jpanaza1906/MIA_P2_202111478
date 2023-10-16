import React, { useState } from 'react';
import Modal from 'react-bootstrap/Modal';

const DescargarImagen = () => {

  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);


  const subReporte = () => {
    var btn = document.getElementById("reportesubmit");
    btn.click();
  }

  const handleDescargarImagen = async () => {
    const nombreImagen = document.getElementById('nreport').value;

    try {
      const response = await fetch(`/reporte/${nombreImagen}`);
      const data = await response.blob();

      // Crear un enlace y hacer clic para descargar
      const url = window.URL.createObjectURL(data);
      const link = document.createElement('a');
      link.href = url;
      link.download = nombreImagen;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (error) {
      console.error('Error al descargar la imagen:', error);
      alert('Error al descargar la imagen.');
    }
  };


  return (
    <div>
      <button className='reportes' onClick={handleShow}> REPORTES </button>{' '}
      <Modal show={show} onHide={handleClose}>
        <div className="reporte-box">
          <form onSubmit={handleDescargarImagen}>
            <div className="user-box">
              <input type="text" name="nombreReporte" id='nreport' required />
              <label>Nombre Reporte</label>
            </div>
            <center>
              <a href='#home' onClick={subReporte}>
                Descargar
                <span></span>
                <input
                  type='submit'
                  id="reportesubmit"
                  style={{ display: 'none' }}
                />
              </a></center>
          </form>
        </div>
      </Modal>
    </div>
  );
};

export default DescargarImagen;
