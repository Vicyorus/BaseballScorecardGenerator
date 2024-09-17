# Changelog

All notable changes to the baseball_scorecard project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Modified the Metapost code to allow for a variable number of innings to be fit.
- Moved the out number labels to the top right corner of the at-bat box to avoid clashes with text on the 1B basepath.
- Extended the functionality of the `Inning.thrown_out` method to record the out in the same base as the runner was in the previous play.

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
