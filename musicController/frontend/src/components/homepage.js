import React, {Component} from "react";
import RoomJoinPage from "./roomjoinpage";
import CreateRoomPage from "./createroompage";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom"; 



export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
            <Router>
                <Routes>
                    <Route exact path = "/" element = {<div><p>This is the home page</p></div>}/>
                    <Route path = "/join" element = {<RoomJoinPage/>} ></Route>
                    <Route path = "/create" element = {<CreateRoomPage/>} ></Route>
                </Routes>
            </Router>

        );
    }
    
}