CHANGELOG.md# Changelog

All notable changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 04/23/2024
This update enhances the Groq AI Toolkit with additional features, improved error handling, and expanded functionality, particularly introducing support for 'LLama 3', JSON mode, and the ability to add a seed for sampling.

### Added
- JSON Output Format: Users can now receive responses in JSON format, making it easier to integrate into applications.
- Seed for Sampling: Adds the ability to specify a seed for deterministic output in sampling, aiding in reproducibility.
- Model Additions: Introduced support for new `LLama3` models, expanding the toolkit's capabilities and model options.

### Fixed
- Improved error handling in the `post` and `stream_post` methods in `client.py` to manage JSON parsing errors and HTTP exceptions more effectively.

### Changed
- Updated model names in the configuration to include `LLama3` versions, reflecting the latest available models.

### Improved
- Enhanced the speed and efficiency of response handling in streamed and post response modes to ensure faster and more reliable outputs.
- Updated documentation and README to reflect new features, improving clarity and user guidance on new options and configurations.

## [1.1.0] - 03/05/2024

### Added
- Initial release.
