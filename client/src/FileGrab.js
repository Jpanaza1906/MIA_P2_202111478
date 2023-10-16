import React, { useState } from "react";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


function FileGrab() {

    const [filePath, setFilePath] = useState('');

    const handleFileInputChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setFilePath(file.name);
            const reader = new FileReader();
            reader.onload = (e) => {
                const filecontent = (e.target.result);
                document.getElementById('editor').value = filecontent;
            }
            reader.readAsText(file);
        }
    };

    const handleButtonClick = () => {
        document.getElementById('fileInput').click();
    };



    const submitCommand = (e) => {
        e.preventDefault();
        // Send the formData as JSON to your server
        const content = document.getElementById('editor').value

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command: content })
        };

        fetch('/command', requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                const consolatextarea = document.getElementById('consola')
                consolatextarea.value = data.response
            })
            .catch(error => console.error('Error:', error));
    }

    return (
        <div>
            <Row className='my-5'></Row>
            <Row className='px-5 my-5 justify-content-md-center'>
                <Col lg="5" className='d-flex align-items-center justify-content-center'>
                    <button onClick={handleButtonClick} id='filebtn'>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" aria-hidden="true">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M13.5 3H12H8C6.34315 3 5 4.34315 5 6V18C5 19.6569 6.34315 21 8 21H11M13.5 3L19 8.625M13.5 3V7.625C13.5 8.17728 13.9477 8.625 14.5 8.625H19M19 8.625V11.8125" stroke="#fffffff" strokeWidth="2"></path>
                            <path d="M17 15V18M17 21V18M17 18H14M17 18H20" stroke="#fffffff" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"></path>
                        </svg>
                        Examinar
                    </button>
                    <input
                        type="file"
                        id="fileInput"
                        onChange={handleFileInputChange}
                        style={{ display: 'none' }}
                    />
                    <div className="input-wrapper">
                        <input
                            type="text"
                            placeholder='Nombre del archivo'
                            name="text"
                            className="input"
                            value={filePath}
                            readOnly
                        />
                    </div>
                </Col>
                <Col md="auto" className='d-flex align-items-center justify-content-center'>
                    <button className="ejecutar" onClick={submitCommand}>EJECUTAR</button>{' '}
                </Col>
            </Row>
        </div>
    );
} export default FileGrab;