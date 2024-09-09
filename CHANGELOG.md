# Changelog

All notable changes to the baseball_scorecard project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

N/A

## [0.1.1] - 2024-09-09

### Added

- Method on `Inning` class for placing a runner on base, `place_runner`.
- Example game for how to tally a strikeout to the original batter on a pinch-hit situation.
- Linked examples repository to README.

### Changed

- Changed the BOS @ PHI 2018-08-14 example game to the LAA @ BOS 2023-04-17 game.

### Fixed

- Issue with defensive substitutions in away team not printed in the correct inning.
- Issue with plays on the basepaths not using a jersey number causing a crash.

## [0.1.0] - 2024-08-27

### Added

- Base code for Python library.
- Usage examples of the library.
- Poetry files for package managing.

[unreleased]: https://github.com/Vicyorus/BaseballScorecardGenerator/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/Vicyorus/BaseballScorecardGenerator/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/Vicyorus/BaseballScorecardGenerator/releases/tag/v0.1.0
