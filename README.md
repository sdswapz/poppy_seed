# Poppy Seed - Android Static Analyzer
![alt text](https://github.com/sdswapz/poppy_seed/blob/master/docs/images/logo.png)

## What is Poppy Seed?

Poppy Seed is an abstraction of malware analysis tool designed for Android OS platform. It provides static analysis capabilities to detect and analyze Android malware, with a focus on discovering security controls enforced by obfuscators, packers, and protectors.

## Why Poppy Seed?

According to Wikipedia, poppy seeds provide 'supposed magical powers of invisibility' - and who doesn't love invisibility, right? Including malware authors! But this Poppy Seed app will help you unveil the magic cloak around malware apps.

## Features

- **File Upload & Analysis**: Drag-and-drop interface for uploading Android APK files
- **Packer Detection**: Identifies 20+ Android protection schemes including:
  - DexProtector, ApkProtector, DexShield, SecNeo
  - Tencent, Baidu, Alibaba protection schemes
  - Bangcle, Jiagu, IJIAMI, and many others
- **Android File Parsing**: Supports APK, DEX, AXML, ARSC file analysis
- **Malware Repository**: Database for storing and browsing analyzed samples
- **Web Interface**: Django-based application with modern UI

## Quick Start

### Prerequisites
- Python 3.9+
- Django 4.2+

### Installation & Setup

#### Option 1: Docker (Recommended)

1. **Install Docker**:
   - macOS: Download [Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - Linux: `sudo apt-get install docker.io docker-compose`
   - Windows: Download [Docker Desktop](https://www.docker.com/products/docker-desktop/)

2. **Clone and run**:
   ```bash
   git clone https://github.com/sdswapz/poppy_seed.git
   cd poppy_seed
   docker-compose up --build
   ```

3. **Access the application**:
   - Main Interface: http://localhost:8000/
   - All features available immediately

#### Option 2: Quick Setup Script

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sdswapz/poppy_seed.git
   cd poppy_seed
   ```

2. **Run the setup script**:
   ```bash
   ./setup.sh
   ```

The setup script will automatically:
- Check Python 3 installation
- Install Django if needed
- Run database migrations
- Start the development server

#### Manual Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sdswapz/poppy_seed.git
   cd poppy_seed/Django
   ```

2. **Install dependencies**:
   ```bash
   pip3 install -r ../requirements.txt
   # OR
   pip3 install django
   ```

3. **Run migrations**:
   ```bash
   python3 manage.py migrate
   ```

4. **Start the development server**:
   ```bash
   python3 manage.py runserver
   ```

#### Access the Application

Once the server is running, access the application at:
- **Main Interface**: http://127.0.0.1:8000/
- **Upload Page**: http://127.0.0.1:8000/
- **About Page**: http://127.0.0.1:8000/about/
- **Repository**: http://127.0.0.1:8000/repo/
- **Admin Panel**: http://127.0.0.1:8000/admin/

### Usage

1. **Upload Files**: Use the drag-and-drop interface to upload Android APK files
2. **Analysis**: The system will automatically analyze the files for:
   - File type detection using magic bytes
   - Packer/protection scheme identification
   - Android manifest parsing
   - Resource file analysis
3. **Results**: View analysis results and browse the malware repository

## Technical Details

- **Backend**: Django 4.2 web framework with SQLite database
- **Frontend**: HTML templates with JavaScript for file uploads
- **Core Parser**: Custom Android file parsers based on Androguard components
- **File Storage**: Organized by date in the media directory
- **Security**: SHA1 hash-based file identification and duplicate detection 

## Development Status

### Current Status (2024)
- ✅ **Phase 1 Complete**: Discovery of security controls enforced (obfuscator, packer, protector)
- ✅ **Core Functionality**: File upload, packer detection, Android file parsing
- ✅ **Web Interface**: Django-based application with modern UI
- ✅ **Database**: SQLite storage with migration support
- 🔄 **Active Development**: Regular updates and improvements

### Development Phases

1. **Phase 1: Security Controls Discovery** ✅ **COMPLETED**
   - Timeline: December 8, 2017 (Released before BSides Philly)
   - Features: Packer detection, file type identification, basic analysis

2. **Phase 2: Static Malware Analysis** 🔄 **IN PROGRESS**
   - Timeline: January 30, 2018 (Planned)
   - Features: Advanced static analysis, malware detection patterns

3. **Phase 3: Dynamic Analysis** 📋 **PLANNED**
   - Timeline: April 8, 2018 (Planned)
   - Features: Dynamic analysis, behavior detection, runtime monitoring

### Contributing

Contributors are always welcome! We need expertise in:
1. **Python Development**: Core application logic and parsers
2. **Malware Analysis**: Security research and detection patterns
3. **Django Frontend**: Web interface and user experience
4. **Docker**: Containerization and deployment
5. **Security Research**: Android malware analysis and reverse engineering

### Recent Updates

- **2024**: Updated to Django 4.2, Python 3.9+ compatibility
- **2024**: Fixed import issues and modernized codebase
- **2024**: Added comprehensive documentation and setup instructions
- **2024**: Enhanced security features and error handling

## Documentation

- **Project Documentation**: [GitHub Pages](https://sdswapz.github.io/poppy_seed/)
- **Docker Setup**: See [DOCKER.md](DOCKER.md) for containerized deployment
- **API Documentation**: Available in the `/docs` directory
- **Security Policy**: See [SECURITY.md](SECURITY.md) for vulnerability reporting
- **Changelog**: See [CHANGELOG.md](CHANGELOG.md) for version history
- **Citation**: See [CITATION.cff](CITATION.cff) for academic citation information

## License

This project is licensed under the **MIT License** - see [LICENSE.md](LICENSE.md) for details.

The MIT License provides maximum freedom for users to:
- Use the software for any purpose
- Modify and distribute the code
- Use it in commercial projects
- Create derivative works

We believe in contributing back to the community by removing barriers to entry. However, all dependencies must comply with their respective licensing agreements. 

## Troubleshooting

### Common Issues

1. **"can't open file 'manage.py'"**:
   ```bash
   # Make sure you're in the Django directory
   cd poppy_seed/Django
   python3 manage.py runserver
   ```

2. **Django Import Errors**:
   ```bash
   # Install Django if not already installed
   pip3 install django
   ```

3. **Database Migration Issues**:
   ```bash
   # Run migrations from the Django directory
   cd poppy_seed/Django
   python3 manage.py migrate
   ```

4. **Port Already in Use**:
   ```bash
   # Use a different port
   python3 manage.py runserver 8080
   ```

### System Requirements

- **Python**: 3.9 or higher
- **Django**: 4.2 or higher
- **Operating System**: macOS, Linux, or Windows
- **Memory**: Minimum 2GB RAM recommended
- **Storage**: 1GB free space for database and uploaded files

## About the Authors

### Contributors
- **Swapnil Deshmukh** - Lead Developer & Security Researcher
- **Sarath Geethakumar** - Co-author & Security Specialist

### Swapnil Deshmukh
![alt text](http://swapnil.me/assets/img/swapnil.jpg)

Swapnil Deshmukh has over 10 years of information technology and information security experience, including technical expertise, leadership, strategy, operational and risk management. Charged with incubating and evangelizing security-driven, context-driven risk management strategies, policies and practices for emerging technologies. 

**Notable Achievements:**
- Co-author of Hacking Exposed series
- Frequent speaker at conferences and roundtables
- Contributor to Health and FinTech publications
- Active in industry peer groups and partnerships

### Sarath Geethakumar

Sarath Geethakumar is a security researcher and practitioner with over 15 years of information security experience. He has co-authored "Hacking Exposed Mobile: Security Secrets & Solutions" and specializes in mobile security research and malware analysis.

## Disclaimer

The views, code, and opinions in this project are those of the authors as independent researchers and do not necessarily reflect the official policy or position of any company. Research on malware analysis is performed based on personal experience and professional connections. This work is not reflective of the position of any individual or company other than the authors.

## Support

- **Issues**: Report bugs and feature requests via GitHub Issues
- **Security**: Report security vulnerabilities via [SECURITY.md](SECURITY.md)
- **Contact**: admin@swapnil.me
- **Documentation**: [GitHub Pages](https://sdswapz.github.io/poppy_seed/)
