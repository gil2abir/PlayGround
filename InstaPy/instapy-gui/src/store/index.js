import createStore from 'unistore';
import { connect as org_connect } from 'unistore/preact';
import actions from './actions';

const initialState = {
	showSidebar: true,
	actions: [],
	token: null,
	usernameInstapy: null
};

const store = createStore(initialState);

const connect = values => org_connect(values, actions);

export {
	actions,
	connect
};

export default store;
