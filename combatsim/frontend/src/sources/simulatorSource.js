import http from './post.js'
import postUrls from '../urls.js'

const SimulatorSource = {
  getCombatants: () => http(postUrls.getCombatants, 'GET'),
  runSimulation: (team1, team2) => http(postUrls.runSimulation, 'POST', {team1, team2})
}

export default SimulatorSource