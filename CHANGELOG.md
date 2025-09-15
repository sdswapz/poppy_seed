# Changelog

All notable changes to Poppy Seed will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Phase 2: Static analysis of Android application to detect malware (Timeline: January 30, 2018)
- Phase 3: Dynamic analysis of Android application to detect malware and its behavior (Timeline: April 8, 2018)
- iOS platform support
- IoT platform support

## [1.0.0] - 2017-12-08

### Added
- Initial release of Poppy Seed Android Static Analyzer
- Django-based web application for malware analysis
- File upload functionality with drag-and-drop support
- Android APK file parsing and analysis
- Android Manifest (AXML) parsing capabilities
- Android Resource (ARSC) file parsing
- DEX file analysis framework
- Packer detection for 20+ Android protection schemes:
  - JSB, AppGuard, DexShield, SecNeo
  - DexProtector, ApkProtector, VKey
  - Arxan GuardIT, Bangcle, Kiro, Jiagu
  - Inside Secure, QBDH, LIAPP, Unicom
  - AppFortify, NQShield, Tencent, IJIAMI
  - NAGA, Alibaba, Pangxie, Medusah
  - Baidu, Kony, Approv
- Magic byte detection for file type identification
- Malware repository database for storing analyzed samples
- Web interface for browsing analyzed samples
- File hash-based duplicate detection
- Support for multiple Android file types (APK, DEX, AXML, ARSC, ELF, SO)

### Technical Details
- Built on Django 1.10.6 framework
- SQLite database for data storage
- Custom Android file parsers based on Androguard components
- File storage organized by date
- SHA1 hash-based file identification
- Support for ZIP-based APK file structure

### Documentation
- Comprehensive README with project overview
- Development timeline and roadmap
- Author information and contributions
- Disclaimer and licensing information

## [0.1.0] - 2017-11-25

### Added
- Initial project setup
- Django project structure
- Basic models for Android analysis
- Initial database migrations
- Basic template structure

## [0.0.1] - 2017-11-20

### Added
- Project initialization
- Repository setup
- Initial documentation structure

---

## Development Timeline

### Phase 1: Discovery of Security Controls ✅
- **Timeline**: December 8, 2017 (Completed)
- **Focus**: Discovery of security controls enforced (obfuscator, packer, protector)
- **Status**: Released before BSides Philly

### Phase 2: Static Analysis (Planned)
- **Timeline**: January 30, 2018
- **Focus**: Static analysis of Android application to detect malware
- **Status**: In development

### Phase 3: Dynamic Analysis (Planned)
- **Timeline**: April 8, 2018
- **Focus**: Dynamic analysis of Android application to detect malware and its behavior
- **Status**: Planned

## Contributing

Contributors are welcome for the following areas:
1. Python development
2. Malware specialist expertise
3. Django front-end development
4. Docker containerization

## Notes

- This is a live repository with commits expected at least every two months
- Currently maintained by a single author with a day job
- Contributors are always welcome
- Development focuses on Android platform first, with plans for iOS and IoT expansion

---

**Legend:**
- ✅ Completed
- 🚧 In Progress
- 📋 Planned
- ❌ Cancelled
