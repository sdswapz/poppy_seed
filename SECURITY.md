# Security Policy

## Supported Versions

This project is currently in active development. Security updates will be provided for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security vulnerability in Poppy Seed, please report it responsibly:

### How to Report

1. **Email**: Send details to [admin@swapnil.me](mailto:admin@swapnil.me)
2. **Subject**: Use "SECURITY: Poppy Seed Vulnerability Report" as the subject line
3. **Include**:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact assessment
   - Any suggested fixes or mitigations

### What to Expect

- **Response Time**: We aim to respond within 48 hours
- **Acknowledgment**: You will receive confirmation that your report was received
- **Updates**: We will provide regular updates on the status of the vulnerability
- **Credit**: Security researchers who responsibly disclose vulnerabilities will be credited (unless they prefer to remain anonymous)

## Security Considerations

### For Users

**⚠️ IMPORTANT SECURITY WARNINGS:**

1. **Malware Handling**: This tool is designed to analyze malware samples. Always:
   - Run Poppy Seed in an isolated environment
   - Use virtual machines or containers
   - Never run on production systems
   - Follow proper malware handling procedures

2. **File Uploads**: The application accepts file uploads for analysis:
   - Only upload files you trust or are specifically analyzing
   - Be aware that malicious files could potentially exploit vulnerabilities in the parser
   - Consider using sandboxed environments

3. **Network Security**: If deploying Poppy Seed:
   - Use HTTPS in production
   - Implement proper access controls
   - Consider network isolation
   - Regularly update dependencies

### For Developers

1. **Dependency Management**: Regularly update all dependencies to address known vulnerabilities
2. **Input Validation**: All file uploads and user inputs should be properly validated
3. **Error Handling**: Avoid exposing sensitive information in error messages
4. **Logging**: Implement comprehensive logging for security monitoring

## Known Security Limitations

1. **File Parsing**: The Android file parsers may have vulnerabilities when processing malformed or malicious files
2. **Django Configuration**: The default Django settings may not be suitable for production use
3. **File Storage**: Uploaded files are stored on the filesystem without additional security measures
4. **Database**: SQLite database may not be suitable for multi-user production environments

## Security Best Practices

### For Deployment

- Use environment variables for sensitive configuration
- Implement proper authentication and authorization
- Use HTTPS with valid certificates
- Regular security updates and patches
- Monitor logs for suspicious activity
- Implement rate limiting for file uploads

### For Development

- Follow secure coding practices
- Regular security code reviews
- Use static analysis tools
- Implement automated security testing
- Keep dependencies updated
- Use secure development frameworks

## Contact Information

- **Security Email**: [admin@swapnil.me](mailto:admin@swapnil.me)
- **Project Maintainer**: Swapnil Deshmukh
- **Co-author**: Sarath Geethakumar

## Acknowledgments

We appreciate the security research community's efforts in helping make Poppy Seed more secure. Thank you for your responsible disclosure practices.

---

**Note**: This security policy is subject to change as the project evolves. Please check back regularly for updates.
