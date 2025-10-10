import 'package:flutter/material.dart'

class ProfileAvatar extends StatelessWidget {
  final String imageUrl;
  const ProfileAvatar({required this.imageUrl, super.key});

  @override
  Widget build(BuildContext context) {
    return CircleAvatar(
      backgroundImage: AssetImage(imageUrl),
    );
  }
}
