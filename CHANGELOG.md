# Changelog

All notable changes to the baseball_scorecard project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2024-11-24

### Added

- Optional argument, `template_dir` in the `Scorecard` class, used to specify a custom folder where different templates for the scorecard may be added.
- Optional argument, `is_risp` in the `Inning.new_ab` method, used to specify that the result of the new at-bat counts for the team's batting average with runners in scoring position statistic.

### Changed

- Modified the Metapost code to allow for a variable number of innings to be fit.
- Moved the out number labels to the top right corner of the at-bat box to avoid clashes with text on the 1B basepath.
- Extended the functionality of the `Inning.thrown_out` method to record the out in the same base as the runner was in the previous play.

### Fixed
- Issue where not specifying the RBIs in a solo home run caused the batter to not get assigned the RBI.
- Issue with reaching on a strikeout adding an additional strike to the pitch count.
- Issue with sacrifice bunts, sacrifice flys and double plays not being tallied when the batter reaches base.
- Issue with sacrifice bunts and sacrifice flys counting as at-bats when tallying at-bats with RISP.
- Issue with minimum of inning columns not being calculated properly, as it didn't account overflowing at-bats that required using the next inning column.

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

[unreleased]: https://github.com/Vicyorus/BaseballScorecardGenerator/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/Vicyorus/BaseballScorecardGenerator/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/Vicyorus/BaseballScorecardGenerator/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/Vicyorus/BaseballScorecardGenerator/releases/tag/v0.1.0
