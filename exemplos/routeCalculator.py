import WazeRouteCalculator
import logging

def calc_route_info(self, real_time=True, stop_at_bounds=False, time_delta=0):
        """Calculate best route info."""

        route = self.get_route(1, time_delta)
        results = route['results' if 'results' in route else 'result']
        route_time, route_distance = self._add_up_route(results, real_time=real_time, stop_at_bounds=stop_at_bounds)
        self.log.info('Time %.2f minutes, distance %.2f km.', route_time, route_distance)
        return route_time, route_distance

logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

from_address = 'Rodovia Sebastião Alves do Nascimento, Rio Paranaíba, MG'
to_address = 'Bahia, Brazil'
route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address)
try:
    route.calc_route_info()
except WazeRouteCalculator.WRCError as err:
    print(err)