import { h, render, Component } from 'preact';
import { NamespacesCard, JobsCard, Settings } from './cards';
import { connect } from 'store';
import { Route } from 'react-router-dom';
import { ConfigService, translate } from 'services';

@connect('actions')
export default class Configuration extends Component {
	componentWillMount() {
		if (!this.props.actions.length) {
			// fetch actions
			ConfigService.fetchActions()
				.then(actions => this.props.setActions(actions));
		}
	}

	render({ match }) {
		return (
			<div>
				<Route
					path={ `${match.url}/namespaces/:namespace?` }
					component={ NamespacesCard }
				/>
				<Route
					path={ `${match.url}/namespaces/:namespace` }
					component={ JobsCard }
				/>
				<Route
					path={ `${match.url}/settings` }
					component={ Settings }
				/>
			</div>
		);
	}
}
