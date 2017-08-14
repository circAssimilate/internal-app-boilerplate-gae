import React from 'react';
import {render} from 'react-dom';
import '../assets/css/styles.scss';
import Button from 'optimizely-oui'


class App extends React.Component {
  render () {
    return (
      <p className="push-double">
        Hello World!
        <Button />
      </p>
    );
  }
}

render(<App/>, document.getElementById('app'));
