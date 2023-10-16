import React from "react";

import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';

function MainTbs() {
    const cleanCommands = () => {
        document.getElementById('editor').value = ''
    };
    const cleanConsole = () => {
        document.getElementById('consola').value = ''
    };

    return (
        <div>
            <Row className='px-5'>
                <Col md="auto" className=' d-flex justify-content-start'>
                    <label id="lbtext">Comandos</label>
                </Col>
                <Col>
                    <button className="clean" onClick={cleanCommands}>
                        <svg viewBox="0 0 448 512" className="svgIcon"><path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"></path></svg>
                    </button>
                </Col>
                <Col md="auto" className=' d-flex justify-content-end'>
                    <button className="clean" onClick={cleanConsole}>
                        <svg viewBox="0 0 448 512" className="svgIcon"><path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"></path></svg>
                    </button>
                </Col>
                <Col md="auto">
                    <label id="lbtext">Consola</label>
                </Col>
            </Row>
            <Row className="px-5 mb-5">
                <Col>
                    <Form.Group className="mb-3">
                        <Form.Control
                            type='text'
                            id="editor"
                            as="textarea"
                            rows={27}
                        />
                    </Form.Group>
                </Col>
                <Col>
                    <Form.Group className="mb-3" >
                        <Form.Control
                            type='text'
                            id="consola"
                            as="textarea"
                            rows={27}
                            readOnly
                        />
                    </Form.Group>
                </Col>
            </Row>
        </div>
    )
} export default MainTbs