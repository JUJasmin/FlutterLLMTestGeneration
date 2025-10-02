import 'package:flutter/material.dart';

class LoginFormValidation extends StatefulWidget {
  const LoginFormValidation({super.key});

  @override
  State<LoginFormValidation> createState() => _LoginFormValidationState();
}

class _LoginFormValidationState extends State<LoginFormValidation> {
  final _formKey = GlobalKey<FormState>();
  final _usernameController = TextEditingController();

  bool get _isValid => _formKey.currentState?.validate() ?? false;

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            key: const Key('username'),
            controller: _usernameController,
            decoration: const InputDecoration(labelText: 'Username'),
            validator: (value) =>
                (value != null && value.contains('@')) ? null : 'Username is email',
          ),
          ElevatedButton(
            key: const Key('submit'),
            onPressed: _isValid ? () {} : null,
            child: const Text('Submit'),
          )
        ],
      ),
    );
  }
}
