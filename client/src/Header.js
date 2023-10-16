import React, {useState} from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Modal from 'react-bootstrap/Modal';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import DescargarImagenes from './DescargarImg';

function Header() {
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const [formData, setFormData] = useState({
        username: '',
        password: '',
        idParticion: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const subLog = () => {
        var btn = document.getElementById("loginsubmit");
        btn.click();
    }

    const submitLogin = (e) => {
        e.preventDefault();
        // Send the formData as JSON to your server
        var logindata = `login -user=${formData.username} -pass=${formData.password} -id=${formData.idParticion}`;
        handleClose()
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command: logindata })
        };



        fetch('/login', requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                const consolatextarea = document.getElementById('consola')
                consolatextarea.value = data.response
            })
            .catch(error => console.error('Error:', error));
    };

    return (
        <header>
            <Navbar collapseOnSelect expand="lg" className="bg-body-tertiary" bg="dark" data-bs-theme="dark" fixed='top'>
                <Container>
                    <Navbar.Brand href="#home">PromptC</Navbar.Brand>
                    <Nav>
                        <Row>
                            <Col>
                                <DescargarImagenes/>
                            </Col>
                            <Col>
                                <button className="login" onClick={handleShow}>Login</button>{' '}
                            </Col>
                        </Row>
                        <Modal show={show} onHide={handleClose}>
                            <div className="login-box">
                                <form onSubmit={submitLogin}>
                                    <div className="user-box">
                                        <input type="text" name="username" required onChange={handleChange} />
                                        <label>Username</label>
                                    </div>
                                    <div className="user-box">
                                        <input type="password" name="password" required onChange={handleChange} />
                                        <label>Password</label>
                                    </div>
                                    <div className="user-box">
                                        <input type="text" name="idParticion" required onChange={handleChange} />
                                        <label>Id Particion</label>
                                    </div>
                                    <center>
                                        <a href='#home' onClick={subLog}>
                                            Login
                                            <span></span>
                                            <input
                                                type='submit'
                                                id="loginsubmit"
                                                style={{ display: 'none' }}
                                            />
                                        </a></center>
                                </form>
                            </div>
                        </Modal>

                    </Nav>
                </Container>
            </Navbar>
        </header>
    );
} export default Header;