import React from "react";
import Container from 'react-bootstrap/Container';

import FileGrab from './FileGrab'
import MainTbs from './MainTbs'

function Main() {
    return (
        <main>
            <Container fluid>
                <FileGrab/>
                <MainTbs/>
            </Container>
        </main>
    );
} export default Main;